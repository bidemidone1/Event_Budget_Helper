# participant_cost
def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)


#event_total
def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    cost = participant_cost(attendees, food_per_person, transport_per_person)

    
    return cost + venue_cost

    cost2 = cost + venue_cost
    
    
#budget_status
def budget_status(budget, total):

    if total <= budget:
        return "Within budget"
    else:
        return "Over budget"

#event_summary             
def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira. {status}."



# Normal attendee count case(normal test case)
cost = participant_cost(10, 800, 200)
print(cost)


cost = participant_cost(10, 600, 400)
print(cost)



cost2 = event_total(10, 800, 200, 5000)
print(cost2)


status1 = budget_status(15000, 15000)
print(status1)


event_name = "Study Day"

summary = event_summary(event_name, cost2, status1)
# print(summary)
print(summary)








