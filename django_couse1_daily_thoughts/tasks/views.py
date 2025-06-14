from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

thoughts = {
    "monday": "A fresh week begins. I choose to enter it with a positive and open mindset. Every Monday is a blank slate—full of potential, possibilities, and moments that can move me closer to my goals. Showing up with intention is half the win.",

    "tuesday": "It doesn't matter when you start—what matters is that you *do*. Tuesday reminds me that action creates momentum. Even small progress breaks inertia and helps keep the wheels turning. Today, I choose to begin, again and again if needed.",

    "wednesday": "Midweek check-in. I'm learning to be more mindful of how I work—staying aware of what energizes me, what needs refinement, and how I can grow through small, consistent improvements. Work is not just output, it's also how I evolve through it.",

    "thursday": "Almost at the week's end—a good time to pause and reflect. Am I working in alignment with my goals, or am I just moving out of habit? Today is about course correction, if needed, and staying true to what matters most in my journey.",

    "friday": "End of the workweek. It's a day to finish strong—clearing out low-effort, high-clutter tasks like timesheets, wrap-ups, and planning. Also, a reminder to celebrate the small wins. If I’ve made progress, I’ve already won. Time to enjoy a little too.",

    "saturday": "A quieter pace. I allow myself to rest but also dedicate time to learning—whether that’s exploring new tech, reading something inspiring, or revisiting personal goals. Saturdays are for planting seeds, both professionally and personally.",

    "sunday": "Reset. I use Sundays to ground myself—spend time with family, reflect in solitude, and prepare for the week ahead. I plan, I prioritize, and I make space for mental clarity and physical well-being. Peace and preparation go hand in hand.",
}

days = list(thoughts.keys())


def index(request):
    # for day in days:
        # day_path=reverse("daily-thoughts",args=[day])
    # list_items += f"<li><a href=\"{day_path}\">{capitalized_day}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    return render(request, "tasks/index.html",{"days":days})

def daily_thoughts(request, day):
    try:
        thought_of_the_day = thoughts[day]
        return render(request, "tasks/tasks.html",{"thought":thought_of_the_day,"day":day.capitalize()})
        # response_thought = render_to_string("tasks/tasks.html")
        # return HttpResponse(response_thought)
    except:
        return HttpResponseNotFound("Enter a valid day to get the thought of the day")
    
def daily_thoughts_by_number(request, day):
    # days = list(thoughts.keys())
    if day > len(days):
        return HttpResponseNotFound("Enter a valid day within 7 to ge a thoughtful thought for the day")
    redirect_day = days[day - 1]
    redirect_path = reverse("daily-thoughts",args=[redirect_day])
    return HttpResponseRedirect(redirect_path)