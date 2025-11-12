class Doctor:
    def __init__(self, name, specialization, timings):
        self.name = name
        self.specialization = specialization
        self.timings = timings

    def __str__(self):
        return f"👨‍⚕️ Dr. {self.name} | {self.specialization} | Available: {self.timings}"


class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __str__(self):
        return f"🧑‍🤝‍🧑 {self.name} | Age: {self.age} | Disease: {self.disease}"


class Appointment:
    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor

    def __str__(self):
        return f"📅 Appointment: {self.patient.name} with Dr. {self.doctor.name} ({self.doctor.specialization})"


class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []

    # Add a new doctor
    def add_doctor(self, name, specialization, timings):
        doctor = Doctor(name, specialization, timings)
        self.doctors.append(doctor)
        print(f"✅ Doctor {name} added successfully!")

    # Register a new patient
    def register_patient(self, name, age, disease):
        patient = Patient(name, age, disease)
        self.patients.append(patient)
        print(f"✅ Patient {name} registered successfully!")

    # Book appointment
    def book_appointment(self, patient_name, doctor_name):
        patient = next((p for p in self.patients if p.name.lower() == patient_name.lower()), None)
        doctor = next((d for d in self.doctors if d.name.lower() == doctor_name.lower()), None)

        if patient and doctor:
            appointment = Appointment(patient, doctor)
            self.appointments.append(appointment)
            print(f"📅 Appointment booked: {patient.name} with Dr. {doctor.name}")
        else:
            print("❌ Either patient or doctor not found!")

    # View all doctors
    def view_doctors(self):
        if not self.doctors:
            print("⚠️ No doctors available.")
        else:
            print("\n=== 🩺 Doctor List ===")
            for doc in self.doctors:
                print(doc)
            print("=====================")

    # View all appointments
    def view_appointments(self):
        if not self.appointments:
            print("⚠️ No appointments booked yet.")
        else:
            print("\n=== 📅 Appointments ===")
            for app in self.appointments:
                print(app)
            print("=======================")


def main():
    hospital = Hospital()
    print("🏥 Welcome to the Hospital Management System")

    while True:
        print("\n========= MENU =========")
        print("1. Add Doctor")
        print("2. Register Patient")
        print("3. Book Appointment")
        print("4. View All Doctors")
        print("5. View All Appointments")
        print("6. Exit")
        print("========================")

        choice = input("Enter your choice (1–6): ").strip()

        if choice == "1":
            name = input("Enter doctor name: ")
            specialization = input("Enter specialization: ")
            timings = input("Enter available timings (e.g., 10AM - 4PM): ")
            hospital.add_doctor(name, specialization, timings)

        elif choice == "2":
            name = input("Enter patient name: ")
            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("⚠️ Age must be a number.")
                continue
            disease = input("Enter disease description: ")
            hospital.register_patient(name, age, disease)

        elif choice == "3":
            patient_name = input("Enter patient name: ")
            doctor_name = input("Enter doctor name: ")
            hospital.book_appointment(patient_name, doctor_name)

        elif choice == "4":
            hospital.view_doctors()

        elif choice == "5":
            hospital.view_appointments()

        elif choice == "6":
            print("👋 Exiting... Thank you for using Hospital Management System!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1–6.")


if __name__ == "__main__":
    main()
