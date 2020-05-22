print("*".center(80, '*'))
print("Welcome to the decision making algorithm for drug resistant epilepsy - \nWritten on Python 3.7.2, Dr Hrishikesh Sarkar MCh")
print("*".center(80, '*'))
print()
print("Enter 0 for none and 1 for yes")
print()
print("Is there a focal lesion on MRI?")

lesion = int(input())

if lesion == 0:
    print("VEEG - Generalised = 0, Focal = 1")
    veeg = int(input())
    if veeg == 0:
        print("Is there localisation on ictal SPECT / PET?")

        ictal = int(input())

        if ictal == 0:
            print("Options include Drugs, DBS, Callosotomy, RNS")
        else:
            print("multifocal = 0, focal = 1")

            multi = int(input())
            if multi == 0:
                print("hemispherotomy")
            else:
                print("Tailored resection or MRgLITT")

    if veeg == 1:
        print("MRgLITT is an option")
# Indentation is important for termination and execution of programme
else:
    print("VEEG - Generalised = 0, Corresonds to lesion = 1")
    veeg = int(input())
    if veeg == 0:
        print("Is there localisation on ictal SPECT / PET?")
        ictal1 = int(input())
        if ictal1 == 0:
            print("Options include Drugs, DBS, Callosotomy, RNS")
        elif ictal1 == 1:
            print("SDG/ECoG - Multifocal / lateralised = 0, Focal = 1")
            SDG = int(input())
            if SDG == 0:
                print("hemispherotomy or multilobar resection")
            else:
                print("Tailored resection or MRgLITT")
    if veeg == 1:
        print("MRgLITT is an option.\n - Is there overlap with eloquent areas on non invasive EEG?")
        overlap = int(input())
        if overlap == 0:
            print("Consider resective surgery or SEEG")
        else:
            print("SEEG guided tailored resection")
print()                
print("*".center(80, '*'))
