import glob
import pandas as pd

def load_subtitles_dataset(dataset_path):
    # Find all .ass files in the dataset directory
    subtitles_paths = glob.glob(dataset_path + '/*.ass')
    scripts = []
    episode_num = []
    
    for path in subtitles_paths:
        try:
            # Read lines with UTF-8 encoding
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                # Skip the first 27 lines (header) and extract relevant parts
                lines = lines[27:]
                lines = [",".join(line.split(',')[9:]) for line in lines]
            
            # Replace '\\N' with a space for proper formatting
            lines = [line.replace('\\N', ' ') for line in lines]
            script = " ".join(lines)
            
            # Extract episode number from the file name
            episode = int(path.split('-')[-1].split('.')[0].strip())
            
            # Append to lists
            scripts.append(script)
            episode_num.append(episode)
        
        except UnicodeDecodeError:
            # If UTF-8 fails, try another encoding (e.g., latin1)
            try:
                with open(path, 'r', encoding='latin1') as file:
                    lines = file.readlines()
                    lines = lines[27:]
                    lines = [",".join(line.split(',')[9:]) for line in lines]
                
                lines = [line.replace('\\N', ' ') for line in lines]
                script = " ".join(lines)
                episode = int(path.split('-')[-1].split('.')[0].strip())
                
                scripts.append(script)
                episode_num.append(episode)
            
            except Exception as e:
                print(f"Failed to process file {path}: {e}")
    
    # Create a DataFrame from the collected data
    df = pd.DataFrame.from_dict({"episode": episode_num, "script": scripts})
    return df