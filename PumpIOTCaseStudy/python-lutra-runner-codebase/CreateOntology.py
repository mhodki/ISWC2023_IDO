from FileIo import clear_output_directory, move_files, read_json_file
from RunLutra import run_lutra_process

def get_ontology_name():
    settings = read_json_file("config/settings.json")
    version_number = settings['ontology_version'].replace(".", "_")
    filename = settings['ontology_filename']
    return f"{filename}_v{version_number}.ttl"

def prepare_output_directory():
    clear_output_directory("config/output")
    move_files("config/imports", "config/output")

if __name__ == "__main__":
    print("Preparing output directory")
    prepare_output_directory()
    print("Running lurta")
    run_lutra_process(get_ontology_name())
    print("Process complete. Please check the config/output folder.")
    input("Press Any Key to Exit...")