lap_year = int(input())

if lap_year % 4 == 0 and lap_year % 100 != 0 or lap_year % 400 == 0:
    print(f"{lap_year} is a leap year")
else:
    print(f"{lap_year} is not a leap year")
    
def lapYear(tahun):
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(lapYear(lap_year))
            