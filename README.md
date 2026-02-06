# 🔋 Wearable Battery Scheduler

A smart task-scheduling algorithm that calculates the **minimum total runtime** for wearable devices by optimizing idle charging periods.

---

## 📖 The "Energy Gap" Logic
This solution uses a **Greedy Algorithm** to minimize time. 
* **Just-in-Time Charging:** Instead of waiting to hit 100%, the device only idles long enough to bridge the gap for the next task.
* **Hardware Safety:** If a task requires more energy than the total battery capacity, the system identifies this impossible constraint and returns `-1.0`.

---

## 📊 Demo Scenario (The 60-Minute Result)
**Inputs:** Capacity: `100` | Initial: `40` | Charge Rate: `1`

| Phase | Duration | Action | Battery Change |
| :--- | :--- | :--- | :--- |
| **Task 1** | 10.0 min | Running Movie | 40% → 10% |
| **Idle** | 40.0 min | **Charging Gap** | 10% → 50% |
| **Task 2** | 10.0 min | Running Meeting | 50% → 0% |
| **TOTAL** | **60.0 min** | | |

## ⚠️ The "Impossible" Scenario (Result: -1.0)
**Inputs:** Capacity: `100` | Initial: `40` | Task: `10, 12`

| Check | Calculation | Logic |
| :--- | :--- | :--- |
| **Energy Needed** | 10s × 12 mAh/s = **120 mAh** | The task requires 120 units. |
| **Max Capacity** | **100 mAh** | The "tank" only holds 100 units. |
| **Result** | **-1.0** | Impossible: Task > Capacity. |

**Why this matters:** This prevents the system from entering an infinite loop or attempting a task that will lead to a hard shutdown mid-execution.

## 🛠️ How to Run
1. Ensure you have **Python 3** installed.
2. Run the script:
   ```bash
   python main.py
