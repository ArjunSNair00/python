#https://ohmyposh.dev/docs/themes
#minimal
#easy-term

# Original command with 'capr4n' as the theme
command = 'oh-my-posh init pwsh --config "C:\\Users\\aryan\\AppData\\Local\\Programs\\oh-my-posh\\themes\\minimal.omp.json" | Invoke-Expression'

# Ask user for new theme name
new_theme = input("Enter the new theme name: ")

# Replace 'capr4n' with the new theme
updated_command = command.replace("minimal", new_theme)

# Output the updated command
print("Updated Command:")
print(updated_command)