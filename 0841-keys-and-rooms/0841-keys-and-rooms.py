class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = list(set(rooms[0]))
        visited=[0]
        while keys:
            a = keys.pop()
            if a not in visited:
                if len(visited)==len(rooms)-1:
                    return True
                visited.append(a)
                keys = list(set(keys + rooms[a]))
        return False