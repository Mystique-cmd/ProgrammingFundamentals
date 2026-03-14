# Import necessary libraries
import asyncio
import heapq
import random
from collections import deque, defaultdict
from datetime import datetime

# Event class
# Represents an emergency event with attributes like type, time step, location, urgency, and proximity
# Computes priority based on urgency, proximity, and type of event
# Implements comparison for priority-based sorting
# Provides a method to compute priority based on urgency, proximity, and type of event
# Implements a less than method to compare priorities of two events
# Allows events to be sorted based on their computed priority
# Initializes with type, time step, location, urgency, and proximity
class Event:
    def __init__(self, type_, time_step, location, urgency, proximity):
        self.type = type_ 
        self.time_step = time_step
        self.location = location
        self.urgency = urgency
        self.proximity = proximity
   
    def ComputePriority(self):
        return 0.4 * self.urgency + 0.4 *( 1 - self.proximity) + 0.2 * ( 1 if self.type == 'medical' else 0.5)
    
    def __lt__(self, other):
        return self.ComputePriority() > other.ComputePriority()  
    
# Dispatcher class
# Manages a queue of events and allows adding and retrieving events based on priority
# Uses a min-heap to efficiently manage event priorities
# Provides methods to add events to the queue and retrieve the next event based on priority
# Initializes with a name and an empty queue
# Adds an event to the queue using a min-heap for priority management
# Retrieves the next event from the queue, returning None if the queue is empty
class Dispatcher:
    def __init__(self, name):
        self.name = name
        self.queue = []  

    def add_event(self, event : Event):
        heapq.heappush(self.queue, event)
 
    def get_next_event(self):
        if self.queue:
            return heapq.heappop(self.queue)
        return None
        
# Scheduler class
# Manages multiple dispatchers and schedules events based on their priority
# Rotates through dispatchers to ensure fair event processing
# Keeps track of the time step and logs dispatched events
# Initializes with a list of dispatchers, sets the initial time step, and prepares an empty log
# Steps through the dispatchers, selecting the event with the highest priority from the current dispatcher
# Logs the dispatched event and updates the time step
class Scheduler:
    def __init__(self, dispatchers):
        self.dispatchers = dispatchers
        self.time_step = 0
        self.log = []
        self.last_index = 0  
    def step(self):
        num_dispatchers = len(self.dispatchers)
        rotated = self.dispatchers[self.last_index:] + self.dispatchers[:self.last_index]
        best_event = None
        best_dispatcher = None

        for dispatcher in rotated:
            if dispatcher.queue:
                event = dispatcher.queue[0]
            if not best_event or event.ComputePriority() > best_event.ComputePriority():
                best_event = event
                best_dispatcher = dispatcher        
                
        if best_dispatcher:
            selected = best_dispatcher.get_next_event()
            self.log.append((self.time_step, best_dispatcher.name, selected.ComputePriority, selected.type))
            print(f"[Time {self.time_step}] Dispatching {selected.type} event from {best_dispatcher.name.upper()} (P={selected.ComputePriority(): .2f})")
        else:
            print(f"Time {self.time_step}: No events to process")
        
        self.last_index = (self.last_index + 1) % num_dispatchers
        self.time_step += 1

# Predictive class
# Monitors the load on each dispatcher and predicts future loads based on historical data
# Uses a deque to maintain a history of the last 10 events for each dispatcher
# Provides methods to update the history with new event counts and predict future loads
# Initializes with an empty history for each dispatcher
# Updates the history with the number of events for a given dispatcher
# Predicts future loads by averaging the historical data for each dispatcher
# Returns a sorted list of dispatchers based on their predicted load
class Predictive:
    def __init__(self):
        self.history = defaultdict(lambda: deque(maxlen=10)) 
    def update(self, dispatcher_name, num_events):
        self.history[dispatcher_name].append(num_events)
    
    def predict(self):
        predicted = {}
        for name, history in self.history.items():
            predicted[name] = sum(history) / len(history) if history else 0
        return sorted(predicted.items(), key=lambda x: -x[1])
    
# Main script
# Initializes dispatchers, scheduler, and predictive model
# Defines asynchronous loops for dispatchers and event generation
# Runs the main event loop to simulate the dispatching system
fire = Dispatcher("Fire")
medical = Dispatcher("Medical")
police = Dispatcher("Police")   
dispatchers = [fire, medical, police]
scheduler = Scheduler(dispatchers)
predictor = Predictive()

# Dispatcher loop
# Continuously checks for events in the dispatcher queue and processes them
# Simulates a delay between handling events to mimic real-world processing time
# Prints the type of event being processed and its computed priority
async def dispatcher_loop(dispatcher: Dispatcher):
    while True:
        if dispatcher.queue:
            event = dispatcher.get_next_event()
            print(f"[DISPATCH]{dispatcher.name} is responding to  {event.type} (P={event.ComputePriority():.2f})")
        await asyncio.sleep(1) # Simulate delay between handling events

# Main function to run the dispatcher loops and event generation
# Uses asyncio to run multiple dispatcher loops concurrently
# Generates events at random intervals and adds them to the appropriate dispatcher queue
# Runs the predictive monitor to forecast dispatcher loads and recommend pre-positioning of resources
async def main():
    await asyncio.gather(
        dispatcher_loop(fire),
        dispatcher_loop(medical),
        dispatcher_loop(police)
    )

# Event generator
# Generates random events at specified time intervals
# Randomly selects event types and attributes like urgency and proximity
# Adds generated events to the appropriate dispatcher queue
# Prints a message when a new event is queued
async def event_generator(dispatchers):
    for t in range(50):
        for _ in range(random.randint(0, 3)):
            e_type = random.choice(['fire', 'medical', 'police'])
            e = Event(e_type, t, location=(random.random(), random.random()),urgency=random.random(), proximity=random.random())
            dispatcher = next(d for d in dispatchers if d.name.lower() == e_type)
            dispatcher.add_event(e)
            print(f"[NEW EVENT] {e_type.upper()} event queued at time {t}")
        await asyncio.sleep(10)

# Predictive monitor
# Continuously monitors the load on each dispatcher and predicts future loads
# Updates the predictive model with the current load of each dispatcher
# Prints upcoming load forecasts and recommends pre-positioning of resources based on predictions
# Runs every 20 seconds to provide updated predictions
async def predictive_monitor(predictor : Predictive, dispatchers):
    while True:
        for d in dispatchers:
            predictor.update(d.name, len(d.queue))
            predictions = predictor.predict()
            print(f"[PREDICTIVE] Upcomiming load forecast {predictions}")

        top_dispatcher, score = predictions[0] 
        print(f"[ALLOCATION] Recommend pre-positioning extra units for {top_dispatcher.upper()} with score (avg load{score:.2f})")
        await asyncio.sleep(20)

# Main function to run the event generator, predictive monitor, and dispatcher loops
# Uses asyncio to run all components concurrently
# Initializes dispatchers, starts the event generator, predictive monitor, and dispatcher loops
# Runs the main event loop to simulate the dispatching system
async def main():
    fire = Dispatcher("Fire")
    medical = Dispatcher("Medical")
    police = Dispatcher("Police")
    dispatchers = [fire, medical, police]
    predictor = Predictive()

    await asyncio.gather(
        event_generator(dispatchers),
        predictive_monitor(predictor, dispatchers),
        dispatcher_loop(fire),
        dispatcher_loop(medical),   
        dispatcher_loop(police),
    )

# Run the main function using asyncio
asyncio.run(main())