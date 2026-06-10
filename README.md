[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=24112833&assignment_repo_type=AssignmentRepo)

# Day 10 Lab: Data Pipeline & Data Observability
## Student Information

- **Student Email:** ngv.chungg@gmail.com
- **Name:** Nguyen Van Chung
- **Student ID:** 2A202600647

---

## Mo ta

Bai lab nay xay dung mot ETL Pipeline don gian de xu ly du lieu san pham tu file `raw_data.json`.

Pipeline thuc hien cac buoc chinh:

1. **Extract:** Doc du lieu tu file JSON.
2. **Validate:** Kiem tra va loai bo du lieu khong hop le.
3. **Transform:** Chuan hoa du lieu, tinh gia sau khi giam 10%, va them timestamp.
4. **Load:** Luu du lieu da xu ly vao file `processed_data.csv`.

Ngoai ra, bai lab con co phan **Data Observability** thong qua viec ghi log so luong record duoc xu ly, so record bi loai, ly do bi loai va thoi gian xu ly. Phan **Agent Simulation** duoc su dung de so sanh ket qua khi agent dung clean data va garbage data.

---

## Cach chay (How to Run)

### Prerequisites

Tao moi truong ao:

```bash
python -m venv venv
```

Kich hoat moi truong ao tren Windows PowerShell:

```bash
.\venv\Scripts\activate
```

Cai dat thu vien can thiet:

```bash
pip install pandas pytest
```

---

### Chay ETL Pipeline

Chay lenh sau de xu ly du lieu tu `raw_data.json` va tao file `processed_data.csv`:

```bash
python solution.py
```

Ket qua da chay thanh cong:

```text
==================================================
ETL Pipeline Started...
==================================================
Extracting data from raw_data.json...
Extract complete. 5 records extracted.
Validation complete. Valid: 3, Errors: 2
Validation summary: 3 kept, 2 dropped.
Errors found: [{'id': 3, 'reason': 'Price <= 0'}, {'id': 4, 'reason': 'Missing Category'}]
Transform complete. 3 records processed.
Data saved to processed_data.csv
Successfully loaded 3 records to processed_data.csv

Pipeline completed! 3 records saved.
```

---

### Tao Garbage Data

Chay lenh sau de tao file du lieu rac `garbage_data.csv`:

```bash
python generate_garbage.py
```

Ket qua:

```text
garbage_data.csv has been created with 'Poisoned' records.
```

---

### Chay Agent Simulation (Stress Test)

Chay lenh sau de test agent voi Clean Data va Garbage Data:

```bash
python agent_simulation.py
```

Neu file `agent_simulation.py` dang tro sai duong dan clean data, can sua duong dan thanh:

```python
"processed_data.csv"
```

Vi du ket qua mong doi:

```text
Testing with CLEAN data:
Agent: Based on my data, the best choice is Laptop at $1200.

Testing with GARBAGE data:
Agent: Based on my data, the best choice is Nuclear Reactor at $999999.
```

Ket qua nay cho thay agent co the dua ra lua chon hop ly khi dung clean data, nhung co the bi danh lua boi garbage data neu du lieu co outlier hoac poisoned record.

---

### Chay Test Tu Dong

Chay lenh sau de kiem tra bai lam bang pytest:

```bash
python -m pytest tests/test_autograder.py -q
```

Ket qua:

```text
9 passed
```

---

## Cau truc thu muc

```text
├── solution.py              # ETL Pipeline script
├── raw_data.json            # Du lieu goc dang JSON
├── processed_data.csv       # Output cua pipeline sau khi xu ly
├── generate_garbage.py      # Script tao garbage data
├── garbage_data.csv         # Du lieu rac dung de stress test
├── agent_simulation.py      # Script mo phong agent voi clean/garbage data
├── experiment_report.md     # Bao cao thi nghiem
├── README.md                # File huong dan va mo ta bai lab
└── tests/
    └── test_autograder.py   # Test cham diem tu dong
```

---

## Ket qua

Pipeline da xu ly thanh cong du lieu tu `raw_data.json`.

Tom tat ket qua:

| Metric                 | Value                |
| ---------------------- | -------------------- |
| Tong so record ban dau | 5                    |
| So record hop le       | 3                    |
| So record bi loai      | 2                    |
| File output            | `processed_data.csv` |
| Test tu dong           | 9 passed             |

Cac record bi loai:

| ID | Ly do            |
| -- | ---------------- |
| 3  | Price <= 0       |
| 4  | Missing Category |

Cac cot moi duoc them vao output:

| Column             | Description                 |
| ------------------ | --------------------------- |
| `discounted_price` | Gia sau khi giam 10%        |
| `processed_at`     | Thoi gian record duoc xu ly |

---

## Data Observability

Bai lab co them cac log de quan sat qua trinh xu ly du lieu:

* So record duoc extract.
* So record hop le.
* So record bi loai.
* Ly do record bi loai.
* So record duoc transform.
* File output sau khi load.
* Timestamp xu ly trong cot `processed_at`.

Data observability giup de dang phat hien loi du lieu va kiem tra chat luong pipeline.

---

## Experiment Summary

Khi su dung `processed_data.csv`, agent dua ra ket qua hop ly vi du lieu da duoc validate va loai bo cac record loi. Khi su dung `garbage_data.csv`, agent co the bi anh huong boi du lieu rac hoac poisoned record, vi du nhu san pham co gia qua lon bat thuong.

Dieu nay cho thay chat luong du lieu anh huong truc tiep den ket qua cua he thong AI/Agent. Vi vay, cac buoc validation, transformation va observability la can thiet truoc khi dua du lieu vao cac he thong tu dong.

---

## Submission

Nop bai len GitHub bang cac lenh sau:

```bash
git add .
git commit -m "feat: hoan thanh bai lab ngay 10"
git push origin main
```

Sau khi push, vao tab **Actions** tren GitHub de kiem tra ket qua cham diem moi nhat.

---

## Final Checklist

* [x] Hoan thanh `solution.py`
* [x] Chay duoc `python solution.py`
* [x] Tao duoc `processed_data.csv`
* [x] Tao duoc `garbage_data.csv`
* [x] Chay duoc `agent_simulation.py`
* [x] Hoan thanh `experiment_report.md`
* [x] Cap nhat `README.md`
* [x] Chay test tu dong thanh cong
* [x] Ket qua pytest: 9 passed
