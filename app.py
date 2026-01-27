import streamlit as st
import pandas as pd

KNOWLEDGE_BASE = [
    {
        "appliance": "Ceiling Fan",
        "condition": "high_usage",
        "tip": "Use fans at medium speed and improve cross-ventilation instead of always running at full speed.",
        "estimated_saving_percent": 10,
        "cost_level": "low"
    },
    {
        "appliance": "LED Bulb",
        "condition": "high_usage",
        "tip": "Turn off lights in common areas when not needed and use natural daylight wherever possible.",
        "estimated_saving_percent": 5,
        "cost_level": "low"
    },
    {
        "appliance": "Washing Machine",
        "condition": "high_usage",
        "tip": "Run washing machines with full loads and use energy-efficient modes if available.",
        "estimated_saving_percent": 5,
        "cost_level": "low"
    }
]


def compute_energy(appliances, residents):
    daily_kwh = 0
    breakdown = []

    for a in appliances:
        
        a_kwh = a["count"] * a["watts"] * a["hours"] / 1000
        daily_kwh += a_kwh
        breakdown.append({
            "name": a["name"],
            "daily_kwh": a_kwh
        })

    monthly_kwh = daily_kwh * 30
    per_resident = monthly_kwh / residents if residents else None
    return monthly_kwh, per_resident, breakdown


def generate_recommendations(breakdown, monthly_bill=None):
    total_daily = sum(b["daily_kwh"] for b in breakdown)
    recs = []

    for b in breakdown:
        share = b["daily_kwh"] / total_daily if total_daily else 0
      
        if share > 0.3:
            cond = "high_usage"
        else:
            continue

        for k in KNOWLEDGE_BASE:
            if k["appliance"] == b["name"] and k["condition"] == cond:
                recs.append({
                    "appliance": b["name"],
                    "tip": k["tip"],
                    "estimated_saving_percent": k["estimated_saving_percent"],
                    "cost_level": k["cost_level"],
                    "share_percent": round(share * 100, 1)
                })

    total_saving_percent = sum(r["estimated_saving_percent"] for r in recs)
 
    total_saving_percent = min(total_saving_percent, 25)

    saving_money = None
    if monthly_bill:
        saving_money = monthly_bill * total_saving_percent / 100

    return recs, total_saving_percent, saving_money


def build_response(context, monthly_kwh, per_resident, recs, total_saving_percent, saving_money):
    lines = []

    lines.append(f"Context: {context}")
    lines.append("")
    lines.append(f"Estimated monthly energy consumption: {monthly_kwh:.1f} kWh.")

    if per_resident is not None:
        lines.append(f"Approximate consumption per resident: {per_resident:.2f} kWh.")

    if not recs:
        lines.append("")
        lines.append("No major high-usage appliances were detected based on the given data.")
        return "\n".join(lines)

    lines.append("")
    lines.append("Key energy-saving recommendations:")

    for i, r in enumerate(recs, 1):
        lines.append(
            f"{i}. {r['appliance']} (≈{r['share_percent']}% of usage): "
            f"{r['tip']} "
            f"(estimated saving: {r['estimated_saving_percent']}%, cost: {r['cost_level']})."
        )

    if saving_money is not None:
        lines.append("")
        lines.append(
            f"Overall, you may save around {total_saving_percent}% on your bill, "
            f"approximately ₹{saving_money:.0f} per month, depending on actual usage."
        )

    return "\n".join(lines)


def main():
    st.title("AI Energy Saver Recommendation Assistant")
    st.write("For Hostels and Households")

    st.sidebar.header("Basic Details")
    place_type = st.sidebar.selectbox("Type", ["Hostel", "Household"])
    residents = st.sidebar.number_input("Number of residents", min_value=1, value=10)
    monthly_bill = st.sidebar.number_input("Monthly bill (₹)", min_value=0, value=8000)

    st.header("Appliance Details")

    st.write("Enter details for each appliance:")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        fan_count = st.number_input("Ceiling fans (count)", min_value=0, value=100)
    with col2:
        fan_watts = st.number_input("Fan watts", min_value=10, value=75)
    with col3:
        fan_hours = st.number_input("Fan hours/day", min_value=0.0, value=10.0)
    with col4:
        pass

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        led_count = st.number_input("LED bulbs (count)", min_value=0, value=100)
    with col6:
        led_watts = st.number_input("LED watts", min_value=1, value=9)
    with col7:
        led_hours = st.number_input("LED hours/day", min_value=0.0, value=8.0)
    with col8:
        pass

    col9, col10, col11, col12 = st.columns(4)
    with col9:
        wm_count = st.number_input("Washing machines (count)", min_value=0, value=1)
    with col10:
        wm_watts = st.number_input("WM watts", min_value=100, value=500)
    with col11:
        wm_hours = st.number_input("WM hours/day", min_value=0.0, value=1.0)
    with col12:
        pass

    appliances = []
    if fan_count > 0:
        appliances.append({"name": "Ceiling Fan", "count": fan_count, "watts": fan_watts, "hours": fan_hours})
    if led_count > 0:
        appliances.append({"name": "LED Bulb", "count": led_count, "watts": led_watts, "hours": led_hours})
    if wm_count > 0:
        appliances.append({"name": "Washing Machine", "count": wm_count, "watts": wm_watts, "hours": wm_hours})

    if st.button("Analyze and Recommend"):
        if not appliances:
            st.error("Please enter at least one appliance.")
        else:
            context = f"{place_type} with {residents} residents and monthly bill ₹{monthly_bill}"
            monthly_kwh, per_resident, breakdown = compute_energy(appliances, residents)
            recs, total_saving_percent, saving_money = generate_recommendations(breakdown, monthly_bill)

          
            st.subheader("Energy Analysis")
            df = pd.DataFrame(breakdown)
            df["share_percent"] = (df["daily_kwh"] / df["daily_kwh"].sum()) * 100
            st.dataframe(df)

            st.subheader("Recommendations (Chat-style)")
            response_text = build_response(context, monthly_kwh, per_resident, recs, total_saving_percent, saving_money)
            st.text(response_text)

if __name__ == "__main__":
    main()

