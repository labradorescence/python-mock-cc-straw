class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, '_name'):
            self._name = name
        else:
            raise Exception
            
    
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip) and new_trip not in self._trips:
            self._trips.append(new_trip)
        return self._trips
    
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor) and new_visitor not in self._visitors:
            self._visitors.append(new_visitor)
        return self._visitors
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        best_visitor = None
        best_record = 0
        for visitor in self._visitors:
            visitor_record = len([trip for trip in self._trips if trip.visitor == visitor])
            if visitor_record > best_record:
                best_record = visitor_record
                best_visitor = visitor
        return best_visitor