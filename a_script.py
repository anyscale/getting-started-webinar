import sys
import ray

def local_func(i):
    return i*i

@ray.remote
def my_remote_task(i):
    return f"The square of {i} is {local_func(i)}"

@ray.remote
class Squarer:
    def squareme(self, i):
        return local_func(i)
    def labelme(self, i):
        ref = my_remote_task.remote(i)
        return ray.get(ref)

if __name__ == "__main__":
    argument = int(sys.argv[1])
    n = local_func(argument)
    actor = Squarer.remote()
    ref = actor.labelme.remote(n)
    print(ray.get(ref))

