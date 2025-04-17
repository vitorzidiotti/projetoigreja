from supabase import create_client, Client

url = "https://qswnqzmikzxlvupvwxra.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFzd25xem1pa3p4bHZ1cHZ3eHJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ2NDIyOTEsImV4cCI6MjA2MDIxODI5MX0.3cB6bVGMDa5DyvRhTzNb9uBisLim-jtnCft4dkfQW9A"

supabase: Client = create_client(url, key)
