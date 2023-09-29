def moveDocsToProjectRoot():
    import shutil
    import os

    docsDir ="docs"
    import os
    if not os.path.exists(docsDir):
        os.makedirs(docsDir)
    source_file = 'routy/html/comparison.html'

    destination_file = 'docs/index.html'  # Name for the file in the project root

    # Move the file to the project root
    shutil.move(source_file, destination_file)

    # Check if the file has been successfully moved
    if os.path.exists(destination_file):
        print(f'The file has been successfully moved to {destination_file}')
    else:
        print('Failed to move the file.')

moveDocsToProjectRoot()