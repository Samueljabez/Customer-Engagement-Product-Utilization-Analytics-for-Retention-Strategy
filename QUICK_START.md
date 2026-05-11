# ⚡ QUICK START GUIDE
## Bank Customer Churn Analysis System

**Get started in 3 easy steps**

---

## 1️⃣ Install Dependencies (2 minutes)

```bash
pip install -r requirements.txt
```

**What gets installed:**
- streamlit (dashboard)
- pandas, numpy (data processing)
- plotly (visualizations)
- scikit-learn (ML utilities)

---

## 2️⃣ Verify Data Files (1 minute)

Check that these files exist in the `data/` folder:
- ✓ `European_Bank.csv` (original dataset)
- ✓ `cleaned_data_with_features.csv` (created by Phase 1)
- ✓ `data_with_engineered_features.csv` (created by Phase 3)
- ✓ `kpi_report.json` (created by Phase 4)

**If missing?** Run the Phase notebooks first:
```bash
jupyter notebook notebooks/Phase_1_Data_Understanding_Cleaning.ipynb
jupyter notebook notebooks/Phase_3_Feature_Engineering.ipynb
jupyter notebook notebooks/Phase_4_KPI_Business_Metrics.ipynb
```

---

## 3️⃣ Launch Dashboard (1 minute)

```bash
streamlit run dashboard/app.py
```

Dashboard opens at: `http://localhost:8501`

---

## 🎯 Dashboard Pages

### 📈 **Page 1: Overview**
- Total customers: 10,000
- Churn rate: 20.37%
- Retention rate: 79.63%
- Active member ratio: 46.35%

**What to look for**: Overall health metrics and KPI summary

---

### 🎯 **Page 2: Engagement Analytics**
- Active customer retention: 86.72%
- Inactive customer retention: 63.40%
- **Key finding**: Active customers 2.75x more likely to stay

**What to look for**: Engagement's impact on churn

---

### 📦 **Page 3: Product Utilization**
- Single product churn: 27.73%
- Multi-product churn: 9.65%
- **Key finding**: More products = lower churn

**What to look for**: Cross-sell opportunities

---

### ⚠️ **Page 4: Premium Risk Detection**
- At-risk premium customers: 980
- Churn rate: 69.28%
- Balance at risk: $65M+
- **Use the filters** to adjust balance/salary thresholds

**What to look for**: Which wealthy customers might leave

---

### 💎 **Page 5: Relationship Strength**
- Sticky customers: 720 (7.2%)
- Sticky customer churn: 0.14%
- **Key finding**: Model to replicate

**What to look for**: Customer loyalty profiles

---

## 🎓 Running Full Analysis (Optional)

Want to see how everything works? Run the notebooks:

```bash
# Open Jupyter
jupyter notebook

# Run these in order:
# 1. Phase_1_Data_Understanding_Cleaning.ipynb (25 min)
# 2. Phase_2_Exploratory_Data_Analysis.ipynb (20 min)
# 3. Phase_3_Feature_Engineering.ipynb (10 min)
# 4. Phase_4_KPI_Business_Metrics.ipynb (10 min)
# 5. Phase_5_Dashboard_Setup.ipynb (5 min)
```

---

## 🔍 Key Insights at a Glance

| Discovery | Impact | Action |
|-----------|--------|--------|
| Active customers are 2.75x more likely to retain | Huge | Launch engagement campaign |
| Multi-product customers churn 65% less | Huge | Cross-sell to single-product customers |
| 980 premium inactive customers = 69% churn | Critical | VIP intervention program |
| 720 sticky customers churn at 0.14% | Best practice | Model for acquisition |

---

## 📊 Dashboard Features

✓ **Real-time Filtering** - Adjust thresholds on Premium Risk page  
✓ **Interactive Charts** - Hover for details, click legend to filter  
✓ **KPI Cards** - Top-line metrics at a glance  
✓ **Data Tables** - Drill-down into customer lists  
✓ **Color Coding** - Red = risk, Green = good  

---

## 🚀 Common Tasks

### "Which customers should I target for retention?"
→ Go to **Page 4: Premium Risk Detection**  
1. Keep balance threshold at $100K
2. Keep salary threshold at $150K
3. See list of at-risk premium customers

### "How much can I improve retention?"
→ Go to **Page 2: Engagement Analytics**  
1. Note: Inactive churn is 36.6%
2. Target: Get to Active level (13.3%)
3. Impact: 3,700 customers × churn reduction × avg balance

### "What's our best customer profile?"
→ Go to **Page 5: Relationship Strength**  
1. See "Sticky Customers" metric: 7.2%
2. 0.14% churn rate (virtually zero)
3. Model this profile in acquisition

---

## ⚙️ Troubleshooting

### Dashboard won't open?
```bash
# Make sure you're in the right directory
cd "Customer engagement for retention strategy"

# Try running with explicit port
streamlit run dashboard/app.py --server.port 8501
```

### Missing data files?
```bash
# Go to notebooks/ and run Phase 1-4 first
cd notebooks
jupyter notebook Phase_1_Data_Understanding_Cleaning.ipynb
```

### Requirements installation fails?
```bash
# Try updating pip first
pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

---

## 📚 Documentation

- **README.md** - Full project documentation
- **PROJECT_SUMMARY.md** - Detailed findings and recommendations
- **QUICK_START.md** - This file!
- **Notebooks** - Step-by-step analysis with explanations

---

## 💡 Pro Tips

1. **Use the dashboard for daily monitoring** - Set as your browser homepage
2. **Export data tables** - Click the download arrow in dashboard tables
3. **Filter by geography** - Check if churn patterns differ by region
4. **Track over time** - Run Phase 4 monthly to monitor KPIs
5. **Share insights** - Dashboard is shareable, works across teams

---

## 🎯 Key Numbers to Remember

- **10,000** customers analyzed
- **20.37%** current churn rate
- **2.75x** engagement impact
- **69.28%** premium inactive churn
- **0.14%** sticky customer churn
- **25-30M** estimated annual retention opportunity

---

## ✅ Success Criteria

You'll know it's working when:
- ✓ Dashboard loads without errors
- ✓ All 5 pages display metrics
- ✓ Charts are interactive (hover, click)
- ✓ Filters work on Premium Risk page
- ✓ Data tables show customer lists

---

## 🎓 Next Steps

1. **Explore the dashboard** (today)
2. **Run the notebooks** (this week)
3. **Share findings with team** (next week)
4. **Design interventions** (next 2 weeks)
5. **Build churn model** (next month)

---

# 🚀 Ready? Let's go!

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

Your dashboard will open at: **http://localhost:8501**

---

**Questions?** Check README.md or PROJECT_SUMMARY.md  
**Want details?** Review the notebooks  
**Ready to present?** Use the dashboard for stakeholder meetings  

**Enjoy! 📊**
