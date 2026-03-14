from faker import Faker
import pandas as pd
import random

fake = Faker('pt_BR')

def generate_sc_data(num_records=500):
    cities = ['Florianópolis', 'Joinville', 'Blumenau', 'Chapecó', 'Criciúma', 'Itajaí']
    sectors = ['SaaS', 'FinTech', 'AgroTech', 'HealthTech', 'EdTech']
    
    data = []
    for _ in range(num_records):
        data.append({
            "cnpj": fake.cnpj(),
            "company_name": fake.company(),
            "city": random.choice(cities),
            "sector": random.choice(sectors),
            "foundation_date": fake.date_between(start_date='-5y', end_date='today'),
            "active_employees": random.randint(1, 150)
        })
    return pd.DataFrame(data)

# Save to the raw folder for the ETL to pick up
df = generate_sc_data()
df.to_csv('data/raw/sc_startups_raw.csv', index=False)