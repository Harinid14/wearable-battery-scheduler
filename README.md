# wearable-battery-scheduler
A Python script to find the fastest way to complete a series of tasks on a device with a limited battery and a charger.
Quick Start
Run the script: python solution.py
Input Example:
Capacity: 100
Initial: 40
Rate: 1
Tasks: 10,3; 10,5
Output: 60.0
How it Works (Simple Logic)
The program acts like a smart manager. It follows these three rules for every task:
Check Capability: Can the battery even hold enough power for this task? If no, it returns -1.0.
Check Current Level: Do we have enough power right now?
Charge if Needed: If we are short on power, we stay Idle just long enough to bridge the gap. We don't waste time charging to 100% unless we have to.
The "60-Minute" Example
Task 1 (Movie): Needs 30 units. We have 40. We start immediately.
Time used: 10 mins. 
Battery left: 10.
Idle (Charging): The next task needs 50 units. We only have 10. We need 40 more.
Time used: 40 mins. 
Battery now: 50.
Task 2 (Meeting): Needs 50 units. We have 50. We finish the task.Time used: 10 mins.Total Time: $10 + 40 + 10 = \mathbf{60.0}$
Key Decisions
Greedy Approach: We only charge what we need. This guarantees the minimum total time.
Error Handling: Returns -1.0 if a task is physically impossible for the hardware.
Precision: Uses floats and rounds to one decimal place for firmware accuracy.
