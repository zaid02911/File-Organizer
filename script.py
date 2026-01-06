import os
import shutil


def main():
    """Main function that orchestrates the file organization process."""
    print("Welcome to your File Organizer!")
    
    # Get organization rules from user
    category_map = get_category_map()
    path = input("Enter your folder path: ")
    
    # Validate path and organize if valid
    if check_path(path):
        organize_files(category_map, path)
        print("File organization completed!")
    else:
        print("Error: Path doesn't exist")


def check_path(path):
    """Check if the provided file path exists."""
    return os.path.exists(path)


def get_files_list(path):
    """Get list of all files and folders in the given directory."""
    return os.listdir(path)


def organize_files(category_map, path):
    """
    Organize files into categorized folders based on file extensions.
    
    Args:
        category_map (dict): Mapping of categories to file extensions
        path (str): Path to the directory to organize
    """
    files_list = get_files_list(path)
    files_moved = 0
    files_skipped = 0
    
    print(f"\nStarting organization of {len(files_list)} items in {path}")
    
    # Ensure 'Other' category exists for uncategorized files
    if 'Other' not in category_map:
        category_map['Other'] = []
        print("Added 'Other' category for uncategorized files")
    
    # Create category folders first
    for category in category_map:
        category_path = os.path.join(path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"📁 Created folder: {category}")
    
    # Organize each file
    for file in files_list:
        file_path = os.path.join(path, file)
        
        # Skip directories (only process files)
        if os.path.isdir(file_path):
            print(f"⏭️  Skipping directory: {file}")
            files_skipped += 1
            continue
        
        # Get file extension for categorization
        file_extension = "." + file.split(".")[-1].lower() if "." in file else ""
        
        # Find which category this file belongs to
        target_category = "Other"
        for category, extensions in category_map.items():
            if file_extension in extensions:
                target_category = category
                break
        
        # Move file to appropriate category folder
        if move_file_to_category(file, file_path, target_category, path):
            files_moved += 1
        else:
            files_skipped += 1
    
    # Print final summary
    print(f"\n=== Organization Summary ===")
    print(f"✅ Files successfully organized: {files_moved}")
    print(f"⏭️  Files skipped: {files_skipped}")


def move_file_to_category(file, file_path, target_category, base_path):
    """
    Move file to target category folder, handling duplicates.
    
    Args:
        file (str): Name of the file to move
        file_path (str): Full path to the file
        target_category (str): Destination category name
        base_path (str): Base directory path
    
    Returns:
        bool: True if file was moved successfully, False otherwise
    """
    try:
        destination_dir = os.path.join(base_path, target_category)
        destination_path = os.path.join(destination_dir, file)
        
        # Case 1: No duplicate - move directly
        if not os.path.exists(destination_path):
            shutil.move(file_path, destination_path)
            print(f"✅ MOVED: {file} → {target_category}/")
            return True
        
        # Case 2: Handle duplicate - create unique filename
        else:
            new_filename = create_unique_filename(file, destination_dir)
            new_destination = os.path.join(destination_dir, new_filename)
            shutil.move(file_path, new_destination)
            print(f"🔄 RENAMED: {file} → {target_category}/{new_filename}")
            return True
            
    except Exception as e:
        print(f"❌ ERROR: Failed to move {file} - {str(e)}")
        return False


def create_unique_filename(filename, destination_dir):
    """
    Create a unique filename when duplicate exists by adding counter.
    
    Args:
        filename (str): Original filename
        destination_dir (str): Target directory
    
    Returns:
        str: Unique filename that doesn't conflict
    """
    name, extension = os.path.splitext(filename)
    counter = 1
    
    # Keep incrementing counter until we find available name
    while True:
        new_filename = f"{name}_copy{counter}{extension}"
        new_path = os.path.join(destination_dir, new_filename)
        
        if not os.path.exists(new_path):
            return new_filename
        counter += 1


def get_category_map():
    """Get file categorization rules from user through interactive menu."""
    print("\n=== Category Setup ===")
    print("1. Use predefined category rules")
    print("2. Create your own category rules manually") 
    print("3. Import category rules from a file")

    choice = input("Enter your choice (1/2/3): ")
    rules_map = {}
    
    if choice == '1':
        rules_map = create_category_rules()
        print("✅ Using predefined category rules")
    elif choice == '2':
        rules_map = create_custom_rules()
        print("✅ Custom category rules created")
    elif choice == '3':
        filename = input("Enter the filename to import rules from: ")
        rules_map = import_rules_from_file(filename)
        if rules_map:
            print("✅ Category rules imported successfully")
    else:
        print("❌ Invalid choice! Using predefined rules as default.")
        rules_map = create_category_rules()
    
    return rules_map


def create_category_rules():
    """Create predefined categories for common file types."""
    return {
        'Documents': ['.pdf', '.docx', '.txt'],
        'Images': ['.jpg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Music': ['.mp3', '.flac', '.wav'],
        'Other': []  # Catch-all for uncategorized files
    }


def create_custom_rules():
    """Interactive function for users to create custom category rules."""
    print("\n=== Custom Rules Setup ===")
    print("Let's create your custom category rules.")

    category_map = {}
    continue_adding_categories = True

    while continue_adding_categories:
        user_input = input("Press 'y' to add a category or 'n' to finish: ").lower()

        if user_input == 'y':
            folder_name = input("Enter category name (e.g., 'Documents'): ")
            category_map[folder_name] = []  
            
            # Add file types to this category
            continue_adding_files = True
            while continue_adding_files:
                user_input = input("Press 'y' to add a file type or 'n' to finish this category: ").lower()

                if user_input == 'y':
                    file_type = input("Enter file extension (e.g., '.png', '.txt'): ")
                    # Ensure extension starts with dot
                    if not file_type.startswith('.'):
                        file_type = '.' + file_type
                    category_map[folder_name].append(file_type)
                    print(f"✅ Added {file_type} to {folder_name}")

                elif user_input == 'n':
                    continue_adding_files = False

        elif user_input == 'n':
            continue_adding_categories = False

    return category_map


def import_rules_from_file(filename):
    """Import category rules from a text file."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            rules = {}
            for line in lines:
                folder_name, file_types = line.strip().split(':')
                file_types = [ft.strip() for ft in file_types.split(',')]
                rules[folder_name] = file_types
            print(f"✅ Imported {len(rules)} categories from {filename}")
            return rules
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return {}


if __name__ == '__main__':
    main()