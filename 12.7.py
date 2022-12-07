# Name: - Neeraj Kumar
# ID: - 2047559

def fat_burning_heart_rate(age):
    return (220 - age)*0.7

#getting the valid age
def get_age(age):
    if (age <= 75 and age >= 18):
        return age
    else:
        raise ValueError("Invalid age.")

try:
    age = int(input())
    get_age(age)
    print("Fat burning heart rate for a", age,
          "year-old:", fat_burning_heart_rate(age), "bpm")
except ValueError as ve:
    print(ve.args[0])
    print("Could not calculate heart rate info.\n")
