import sys, os, re, subprocess

# Function to extract the time from the output
def extractTime(output, part):
    """Extracts time for the specified part from the output."""
    match = re.search(f'{part} Time: ([0-9]+)', output)
    if match:
        return int(match.group(1))
    return None

def benchmark(file, runs=100):
    """Run the day file multiple times and collect times."""
    times1 = []
    times2 = []
    
    for _ in range(runs):
        # Run the Python file and capture its output
        result = subprocess.run(['python', file], capture_output=True, text=True)
        
        if result.returncode == 0:
            output = result.stdout
            # Extract times for both parts
            part1 = extractTime(output, "Part 1")
            part2 = extractTime(output, "Part 2")
            
            if part1 is not None:
                times1.append(part1)
            if part2 is not None:
                times2.append(part2)
    
    # Calculate average and best times
    avg1 = sum(times1) / len(times1) if times1 else 0
    avg2 = sum(times2) / len(times2) if times2 else 0
    best1 = min(times1) if times1 else 0
    best2 = min(times2) if times2 else 0
    
    return avg1, best1, avg2, best2

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        day = 1
        end = 26
        print("Benchmarking all days, avg and best times of 100 repetitions in microseconds")
    else:
        day = int(sys.argv[1])
        end = day+1
        print(f"Benchmarking day {day}, avg and best times of 100 repetitions in microseconds")
        
    print("\t\t\tAverage\t\tBest")
    
    basePath = os.getcwd()
    
    # For Each Day
    for i in range(day, end):
        dayFolderPath = os.path.join(basePath, f"Day {i}")
        if os.path.isdir(dayFolderPath):
            print(f"Day {"0" + str(i) if i < 10 else i}:")
                    
            dayFilePath = os.path.join(dayFolderPath, f"day{i}.py")                
            os.chdir(dayFolderPath)
            
            # Benchmark q1 and q2
            avg1, best1, avg2, best2 = benchmark(dayFilePath)
            
            print(f"\tPart 1:\t\t{round(avg1)} us\t{"\t" + str(round(best1)) if len(str(round(avg1))) < 5 else str(round(best1))} us")
            print(f"\tPart 2:\t\t{round(avg2)} us\t{"\t" + str(round(best2)) if len(str(round(avg2))) < 5 else str(round(best2))} us")
                
            os.chdir(basePath)