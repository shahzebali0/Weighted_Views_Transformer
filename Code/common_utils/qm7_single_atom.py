import numpy as np
np.random.seed(42)


def small_views(vs, piece_size=4):
    """
    Split views into smaller pieces such that each small view contains only atomic number + 3D coordinates.

    Parameters:
    - vs: numpy array of views
    - piece_size: size of each small view (default = 4: atomic number + 3D coordinates)
    
    Returns:
    - new_view: numpy array with views split into atomic pieces
    """
    # Check that the view size is divisible by the piece size
    if vs.shape[-1] % piece_size != 0:
        raise ValueError(f"View size {vs.shape[-1]} is not divisible by piece size {piece_size}.")
    
    single_atom_piece = vs.shape[-1] // piece_size
    
    new_view = np.reshape(vs, (vs.shape[0], vs.shape[1], single_atom_piece, piece_size))
    
    return new_view
# sources 
# Electron affinity : https://periodictable.com/Properties/A/ElectronAffinity.v.log.html
# Electronegativity :https://periodictable.com/Properties/A/Electronegativity.al.html
# Valence electron: https://periodictable.com/Properties/A/Valence.al.html
# covalent radius: https://periodictable.com/Properties/A/CovalentRadius.an.html
# First ionization energy: https://periodictable.com/Properties/A/IonizationEnergies.an.html
# Atomic volume: http://hyperphysics.phy-astr.gsu.edu/hbase/pertab/H.html
# Dictionary containing properties for each atom type


atom_properties = {
    "H": {
        "electronegativity": 2.20, "atomic_mass": 1.008, "valence_electrons": 1,
        "group_number": 1, "covalent_radius": 31, "first_ionization_energy": 13.59,
        "electron_affinity": 0.754, "atomic_volume": 14.0
    },
    "C": {
        "electronegativity": 2.55, "atomic_mass": 12.01, "valence_electrons": 4,
        "group_number": 14, "covalent_radius": 76, "first_ionization_energy": 11.26,
        "electron_affinity": 1.263, "atomic_volume": 4.58
    },
    "N": {
        "electronegativity": 3.04, "atomic_mass": 14.007, "valence_electrons": 5,
        "group_number": 15, "covalent_radius": 71, "first_ionization_energy": 14.534,
        "electron_affinity": 0.07, "atomic_volume": 17.3
    },
    "O": {
        "electronegativity": 3.44, "atomic_mass": 15.999, "valence_electrons": 6,
        "group_number": 16, "covalent_radius": 66, "first_ionization_energy": 13.618,
        "electron_affinity": 1.461, "atomic_volume": 14
    },
    "S": {
        "electronegativity": 2.58, "atomic_mass": 32.06, "valence_electrons": 6,
        "group_number": 16, "covalent_radius": 105, "first_ionization_energy": 10.360,
        "electron_affinity": 2.077, "atomic_volume": 15.5
    },
    "F": {
        "electronegativity": 3.98, "atomic_mass": 18.998, "valence_electrons": 7,
        "group_number": 17, "covalent_radius": 57, "first_ionization_energy": 17.423,
        "electron_affinity": 3.339, "atomic_volume": 17.1
    },
    "P": {
        "electronegativity": 2.19, "atomic_mass": 30.974, "valence_electrons": 5,
        "group_number": 15, "covalent_radius": 107, "first_ionization_energy": 10.487,
        "electron_affinity": 0.745, "atomic_volume": 17.0
    },
    "Cl": {
        "electronegativity": 3.16, "atomic_mass": 35.45, "valence_electrons": 7,
        "group_number": 17, "covalent_radius": 102, "first_ionization_energy": 12.968,
        "electron_affinity": 3.617, "atomic_volume": 22.7
    },
    "Br": {
        "electronegativity": 2.96, "atomic_mass": 79.904, "valence_electrons": 7,
        "group_number": 17, "covalent_radius": 120, "first_ionization_energy": 11.814,
        "electron_affinity": 3.365, "atomic_volume": 23.5
    },
    "I": {
        "electronegativity": 2.66, "atomic_mass": 126.90, "valence_electrons": 7,
        "group_number": 17, "covalent_radius": 139, "first_ionization_energy": 10.451,
        "electron_affinity": 3.059, "atomic_volume": 25.7
    }
  

}

# Switch for atomic properties
single_atomic_property_switches = {
    "electronegativity": True,
    "atomic_mass": True,
    "valence_electrons": True,
    "group_number": True,
    "covalent_radius": True,
    "first_ionization_energy": True,
    "electron_affinity": True,
    "atomic_volume": True
}


atomic_number_to_type = {
    1: "H",
    6: "C",
    7: "N",
    8: "O",
    9: "F",
    15: "P",
    16: "S",
    17: "Cl",
    35: "Br",
    53: "I"
}


def get_embeddings(single_atom, atom_properties, single_atomic_property_switches, embedding_size=16):
    """
    Get fixed-size embeddings (length=16) for each atom using atomic number, 3D coordinates, and selected properties.
    Remaining positions are zero-padded.

    Parameters:
    - single_atom: numpy array (N_molecules, N_views, N_atoms, 4)
    - atom_properties: dictionary of properties per atom type
    - single_atomic_property_switches: which properties to include
    - embedding_size: desired fixed embedding length (default = 16)

    Returns:
    - atom_embeddings: numpy array (N_molecules, N_views, N_atoms, embedding_size)
    """
    number_of_molecules = single_atom.shape[0]
    number_of_views = single_atom.shape[1]
    number_of_atoms = single_atom.shape[2]
    
    property_keys = [prop for prop, is_on in single_atomic_property_switches.items() if is_on]
    num_features = 1 + 3 + len(property_keys)  # atomic_number + coordinates + properties

    if num_features > embedding_size:
        raise ValueError(f"Embedding size {embedding_size} is too small for selected features (requires at least {num_features}).")

    atom_embeddings = []

    for mol_id in range(number_of_molecules):
        molecule_extended = []
        for view_id in range(number_of_views):
            view = single_atom[mol_id, view_id]
            view_extended = []

            for atom_id in range(number_of_atoms):
                atomic_number = view[atom_id, 0]

                if atomic_number == 0.0:
                    extended_atom = np.zeros(embedding_size)
                else:
                    coord = view[atom_id, 1:4]
                    atom_type = atomic_number_to_type.get(atomic_number, "H")  # default to H if unknown
                    properties = [atom_properties[atom_type][prop] for prop in property_keys]
                    raw_features = np.concatenate([[atomic_number], coord, properties])

                    # Pad with zeros to reach desired embedding size
                    padded = np.zeros(embedding_size)
                    padded[:len(raw_features)] = raw_features
                    extended_atom = padded

                view_extended.append(extended_atom)
            molecule_extended.append(np.array(view_extended))
        atom_embeddings.append(np.array(molecule_extended))

    return np.array(atom_embeddings)