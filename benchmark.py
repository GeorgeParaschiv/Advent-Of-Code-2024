import os, importlib.util, time

# Function to dynamically import a module from a file path
def importFunction(filePath, funcName):
    spec = importlib.util.spec_from_file_location("module", filePath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, funcName)

# Function to benchmark another function
def benchmark(func, runs=100):
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append(end - start)
    
    times = [time for time in times if time > 0]
    
    # Calculate average and best times in microseconds
    avg = sum(times)/len(times) * 1000000
    best = min(times) * 1000000
    
    return avg, best

if __name__ == "__main__":
    print("Benchmarking all days, avg and best times of 100 repetitions in microseconds")
    print("\t\t\tAverage\t\tBest")
    
    basePath = os.getcwd()
    
    # For Each Day
    for i in range(1, 26):
        dayFolderPath = os.path.join(basePath, f"Day {i}")
        if os.path.isdir(dayFolderPath):
            print(f"Day {"0" + str(i) if i < 10 else i}:")
            
            # Import the functions q1 and q2 from the day file
            try:
        
                dayFilePath = os.path.join(dayFolderPath, f"day{i}.py")
                
                q1 = importFunction(dayFilePath, 'q1')
                q2 = importFunction(dayFilePath, 'q2')
                
                os.chdir(dayFolderPath)
                
                # Benchmark q1 and q2
                avg1, best1 = benchmark(q1)
                avg2, best2 = benchmark(q2)
                
                print(f"\tPart 1:\t\t{round(avg1)} us\t{"\t" + str(round(best1)) if len(str(round(avg1))) < 5 else str(round(best1))} us")
                print(f"\tPart 2:\t\t{round(avg2)} us\t{"\t" + str(round(best2)) if len(str(round(avg2))) < 5 else str(round(best2))} us")
                
            except Exception as e:
                print(f"Error importing functions from {dayFilePath}: {e}")
            finally:
                os.chdir(basePath)