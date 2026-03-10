import calendar
import turtle
from datetime import datetime

# Setup turtle screen
screen = turtle.Screen()
screen.setup(width=1200, height=900)
screen.bgcolor("black")
screen.title("3D Calendar")
turtle.screensize(1200, 900)
turtle.speed(0)
turtle.hideturtle()

# Colors
WHITE = "white"
CYAN = "cyan"
MAGENTA = "magenta"
GOLD = "gold"
ORANGE = "orange"

def draw_3d_text(text, x, y, color=WHITE, size=20, angle=0):
    """Draw text with 3D effect"""
    # Draw shadow layers for 3D effect
    for i in range(5, 0, -1):
        turtle.penup()
        turtle.goto(x - i, y - i)
        turtle.color("gray20")
        turtle.write(text, align="center", font=("Arial", size, "bold"))
    
    # Draw main text
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(text, align="center", font=("Arial", size, "bold"))

def draw_vertical_text(text, x, y, color=WHITE, size=20):
    """Draw text vertically with 3D effect - centered"""
    # Calculate total height needed
    char_count = len(text)
    total_height = char_count * (size + 5)
    start_y = y + total_height // 2
    
    # Draw shadow layers for 3D effect
    for i in range(5, 0, -1):
        turtle.penup()
        turtle.goto(x - i, start_y - i)
        turtle.setheading(-90)
        turtle.color("gray20")
        for char in text:
            turtle.write(char, align="center", font=("Arial", size, "bold"))
            turtle.forward(size + 5)
        turtle.setheading(0)
    
    # Draw main text
    turtle.penup()
    turtle.goto(x, start_y)
    turtle.setheading(-90)
    turtle.color(color)
    for char in text:
        turtle.write(char, align="center", font=("Arial", size, "bold"))
        turtle.forward(size + 5)
    turtle.setheading(0)

def draw_3d_box(x, y, width, height, color=WHITE):
    """Draw a 3D box effect"""
    turtle.penup()
    
    # Draw back shadow
    turtle.goto(x - 5, y - 5)
    turtle.pendown()
    turtle.color("gray20")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    
    # Draw front face
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.width(2)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def get_month_data(year, month):
    """Get calendar data for a specific month"""
    month_name = calendar.month_name[month]
    cal = calendar.monthcalendar(year, month)
    return month_name, cal

def draw_month(month_name, cal, start_x, start_y, month_num):
    """Draw a single month in 3D style"""
    # Draw month name with 3D effect
    colors = [CYAN, MAGENTA, GOLD, ORANGE, "lime", "coral", 
              "mediumpurple", "yellow", "hotpink", "lightblue", "salmon", "plum"]
    
    draw_3d_text(month_name, start_x + 75, start_y, colors[month_num-1], 16)
    
    # Draw days header
    days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    for i, day in enumerate(days):
        turtle.penup()
        turtle.goto(start_x + i * 22 + 10, start_y - 25)
        turtle.color("white")
        turtle.write(day, align="center", font=("Arial", 8, "bold"))
    
    # Draw calendar days
    row = 0
    for week in cal:
        col = 0
        for day in week:
            if day != 0:
                x_pos = start_x + col * 22 + 10
                y_pos = start_y - 45 - row * 22
                
                # Draw 3D effect for each day
                turtle.penup()
                turtle.goto(x_pos + 3, y_pos - 3)
                turtle.color("gray30")
                turtle.write(str(day), align="center", font=("Arial", 9, "bold"))
                
                turtle.goto(x_pos, y_pos)
                # Highlight weekends
                if col >= 5:
                    turtle.color("salmon")
                else:
                    turtle.color("white")
                turtle.write(str(day), align="center", font=("Arial", 9, "bold"))
            col += 1
        row += 1

def draw_3d_calendar(year):
    """Draw the complete 3D calendar for a year"""
    turtle.clear()
    
    # Draw title vertically - left side, smaller and darker (behind months)
    draw_vertical_text(f"Calendar {year}", -530, 0, "gray40", 22)
    
    # Draw decorative lines
    turtle.penup()
    turtle.goto(-500, 350)
    turtle.pendown()
    turtle.color(CYAN)
    turtle.width(3)
    turtle.forward(1000)
    
    turtle.penup()
    turtle.goto(-500, -380)
    turtle.pendown()
    turtle.forward(1000)
    
    # Calculate positions for 12 months (4 rows x 3 columns)
    months_per_row = 3
    x_offset = -400
    y_offset = 280
    x_spacing = 270
    y_spacing = 175
    
    for month in range(1, 13):
        row = (month - 1) // months_per_row
        col = (month - 1) % months_per_row
        
        start_x = x_offset + col * x_spacing
        start_y = y_offset - row * y_spacing
        
        # Draw border box for each month (commented to remove grey box)
        # draw_3d_box(start_x - 5, start_y + 30, 155, 115, "gray30")
        
        # Get and draw month data
        month_name, cal = get_month_data(year, month)
        draw_month(month_name, cal, start_x, start_y, month)
    
    # Draw footer
    turtle.penup()
    turtle.goto(0, -420)
    turtle.color("gray")
    turtle.write("Close window to exit", align="center", font=("Arial", 10, "normal"))

# Main program
if __name__ == "__main__":
    try:
        # Get year from user
        print("=" * 50)
        print("       3D CALENDAR GENERATOR")
        print("=" * 50)
        year = int(input("Enter year: "))
        print(f"Generating 3D calendar for year {year}...")
        print("A turtle graphics window should open...")
        
        # Clear any previous text
        turtle.clear()
        
        # Draw the 3D calendar
        draw_3d_calendar(year)
        
        # Print completion message
        print(f"\n3D Calendar for {year} has been generated!")
        print("Please check the turtle graphics window")
        
        # Keep window open
        turtle.done()
        
    except ValueError:
        print("Error: Please enter a valid year (e.g., 2030)")
    except Exception as e:
        print(f"Error: {e}")
