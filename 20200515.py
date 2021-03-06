# Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.


# Implement a "timed" map, where each key in the map can be assigned to different values at different times. Lookups are then performed at specific timestamps.

# map.set("key1", "value1", 4);
# map.set("key1", "value2", 6);
# map.set("key1", "value3", 100);
# map.set("otherKey", "someValue", 100);

# map.get("key1", 3); // should return null/None or throw an exception
# map.get("key1", 5); // should return value1
# map.get("key1", 99); // should return value2

# {key1: [{value:value1, time:4}, {value:value2, time: 6}]

from operator import attrgetter
class TimeMap:
  def __init__(self):
    self.items = {}

  def set(self, key, value, time):
    if key in self.items:
      self.items[key].append({value: value, time: time})
      self.items[key].sort(key=attrgetter('time'))
    else:
      self.items[key] = [{value: value, time: time}]

  def get(self, key, time):
    if key not in self.items or self.items[key][0].time > time:
      return None
    values = self.items[key]
    start = 0
    end = len(values) - 1
    while start <= end:
      mid = (start + end) // 2
      if values[mid].time == time:
        return values[mid].value
      if values[mid].time < time:
        if mid+1 < len(values) and values[mid+1].time > time:
          return values[mid].value
        start = mid+1
      else:
        # values[mid].time > time
        if mid-1 >= 0 and values[mid-1].time < time:
          return values[mid-1].value
        end = mid-1
    return None
          
        
