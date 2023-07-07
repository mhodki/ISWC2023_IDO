import subprocess
import os
def run_lutra_process(ontology_filename):

    filenames = os.listdir("config/templates/bottr/")
    full_filenames = [f"templates/bottr/{filename}" for filename in filenames]
    filenames_string = ' '.join(full_filenames)

    outputType = "wottr"
    outputFolder = "output/"
    outputFilename = ontology_filename
    libraryType = "stottr"
    libraryFolder = "templates/stottr"
    inputType = "bottr"
    inputFolder = filenames_string

    command = "java -jar lutra.jar -m expand -O " \
        + outputType + " -o " + outputFolder + outputFilename \
        + " -L " + libraryType + " -l " \
        + libraryFolder \
        + " -I " + inputType \
        + " " + inputFolder \
        + " --fetchMissing" \
        #+ " --quiet" \
    
    result = subprocess.run(command
        , stdout=subprocess.PIPE
        , stderr=subprocess.PIPE
        , shell=True
        , cwd="config")
        
    print(result.stderr.decode("utf-8"))
    