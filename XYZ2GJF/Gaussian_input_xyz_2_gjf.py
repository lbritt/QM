import os


def read_xyz_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_atoms = int(lines[1])
        coordinates = []
        for line in lines[3:]:
            split_line = line.split()
            symbol, x, y, z = split_line[0], float(split_line[1]), float(split_line[2]), float(split_line[3])
            coordinates.append([symbol, x, y, z])
        return coordinates


def generate_gaussian_input(file_name, coordinates, frozen_atoms, dir_path, subdirectory_path):
    with open(os.path.join(subdirectory_path, file_name + '.gjf'), 'w') as f:
        f.write(f"%nprocshared=32\n%mem=96GB\n%chk={file_name}.chk\n")
        f.write(f"#p M062X/def2SVP opt=modredundant geom=connectivity empiricaldispersion=gd3 scrf=(smd,solvent=dichloromethane) NoSymm\n\n")
        f.write(f"{file_name}\n\n")
        f.write("1 2\n")
        for i, coord in enumerate(coordinates):
            f.write(str(coord[0]) + " ")
            if i in frozen_atoms:
                f.write(" -1 ")
            else:
                f.write(" 0 ")
            symbol, x, y, z = coord[0], coord[1], coord[2], coord[3]
            f.write(f"{x:.6f} {y:.6f} {z:.6f}\n")
        f.write(f"\n")
    with open(os.path.join(subdirectory_path + '\\run.sh'), 'w') as f:
        f.write(f'#!/bin/bash\n#SBATCH --job-name=gaussian_run\n')
        f.write(f'#SBATCH --mem-per-cpu=3000M\n')
        f.write(f'#SBATCH --cpus-per-task=32\n')
        f.write(f'#SBATCH --ntasks=1\n')
        f.write(f'#SBATCH --time=00-24:00\n')
        f.write(f'module load gaussian/g16.c01\n')
        f.write(f'g16 < {file_name}.gjf >& {file_name}.log\n')  # add the name of the .gjf file here
        f.write(f'formchk {file_name}.chk {file_name}.fchk\n')


def main():
    xyz_files = [f for f in os.listdir() if f.endswith('.xyz')]

    for xyz_file in xyz_files:
        xyz_name = xyz_file.split('.')[0]

        if "_" in xyz_name:
            parts = xyz_name.split('_')
            if len(parts) == 3:
                directory = parts[0]
                subdirectory = f"{parts[1]}/{parts[2]}"
                os.makedirs(f"{directory}/{subdirectory}", exist_ok=True)
                coords = read_xyz_file(xyz_file)
                generate_gaussian_input(xyz_name, coords, [], directory, f"{directory}/{subdirectory}")
            elif len(parts) == 2:
                directory = parts[0]
                subdirectory = f"{parts[1]}"
                os.makedirs(f"{directory}/{subdirectory}", exist_ok=True)
                coords = read_xyz_file(xyz_file)
                generate_gaussian_input(xyz_name, coords, [], directory, f"{directory}/{subdirectory}")
            else:
                print(f"Invalid filename format for file {xyz_name}. Skipping...")
        else:
            directory = xyz_name
            os.makedirs(directory, exist_ok=True)
            coords = read_xyz_file(xyz_file)
            generate_gaussian_input(xyz_name, coords, [], directory, directory)

if __name__ == '__main__':
    main()
#
