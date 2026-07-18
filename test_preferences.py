from database import save_preferences, get_preferences

save_preferences("college", "HICAS")
save_preferences("language", "Python")
save_preferences("voice", "Female")


print(get_preferences())