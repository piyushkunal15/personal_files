import csv
import random

file_name = "output.csv"
networth_start = 481  # Initial net worth
salary = 0
total_yearly_expense = 9.5  # Base yearly expense
conversative_yearly_expense = 8
startup_investment_yearly = 0
taxes = 1
failed = False
write = True
total_growth = 0
total_inflation = 0
with open(file_name, mode='w', newline='') as file:
    if write:
        writer = csv.writer(file)
    
    # Write the header row
    if write:
        writer.writerow(["Year number", "Networth Start", "Total expense", "Taxes","Inflation %", "Networth Growth %", "Startup investment","Salary","Networth left",])
    
    networth_left = networth_start

    for year in range(1, 61):
        if year > 1:
            salary = 0
        # Generate random inflation between 5% and 10% (weighted towards 5-7%)
        rand = random.randint(0, 99)
        if rand < 80:
            inflation = random.uniform(5, 8)  # 5-7 (higher weightage)
        else:
            inflation = random.uniform(4, 10)  # 8-10 (lower weightage)

        
        # Generate random net worth growth between 4% and 16% (weighted towards 7-10%)
        growth_rand = random.randint(0, 99)
        if growth_rand < 70:
            growth = random.uniform(2, 14)  # 7-10 (higher weightage)
        else:
            growth = random.uniform(3, 18)  # 4-16 (normal weightage)

        if year > 25:
            growth = 7

        total_growth +=  growth 
        total_inflation +=  inflation
        
        # Apply inflation to yearly expense
        total_yearly_expense = round(total_yearly_expense * (1 + inflation / 100.0), 2)
        conversative_yearly_expense = round(conversative_yearly_expense * (1 + inflation / 100.0), 2)
        taxes = round(taxes * (1 + inflation / 100.0), 2)


        considered_expense = total_yearly_expense
        if year > 20:
            considered_expense = conversative_yearly_expense
        
        # Write current year data
        if write:
            writer.writerow([year, round(networth_left, 2), considered_expense, taxes, round(inflation,2), round(growth, 2), round(startup_investment_yearly,2),salary, ""])
        
     

        # Update net worth for next year
        networth_left = round((networth_left - considered_expense - startup_investment_yearly - taxes) * (1 + growth / 100.0), 2)
        salary = round(salary * 1.07,2)
        networth_left += salary

        if year == 45 or year == 3:
            print(f"Networth left at :" + str(year) + " years: " + str(networth_left))


        if write:
            writer.writerow(["", "", "", "", "", "", "","", networth_left])
        startup_investment_yearly = startup_investment_yearly/2
        if (networth_left < 0):
            print(f"Networth exhaused at year: {year}")
            failed = True
            break
if not failed:
    print(f"Networth sufficed for 60 years and left: {networth_left}")
print(f"Average growth :" + str(round(total_growth/year, 2)) + " Average inflation: "+str(round(total_inflation/year,2)))
