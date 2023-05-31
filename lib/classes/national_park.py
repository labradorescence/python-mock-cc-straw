class NationalPark:

    #INITIALIZERS

    def __init__(self, name):
        self._name = name
        self._trips = []
        self._visitors = []
    
    #PROPERTIES
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception
    
    #OBJECT RELATIONSHIP METHODS & PROPERTIES
    
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if new_visitor and new_visitor not in self._visitors and isinstance(new_visitor, Visitor) :
            self._visitors.append(new_visitor)
        return self._visitors
    
    #AGGREGATE & ASSOCIATION METHODS
    
    def total_visits(self):
        return len(self._trips)
            
    def best_visitor(self):
        best_visitor = None
        trip_record = 0
        for visitor in self._visitors:
            trip_count = len([trip for trip in self._trips if trip.visitor == visitor])
            if trip_count > trip_record:
                best_visitor = visitor
                trip_record = trip_count
        return best_visitor