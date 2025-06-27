import concurrent.interpreters as interpreters

interp = interpreters.create()

a = 15
print(f"A in main: {a}")

try:
    interp.exec('print("Hello from PEP-734")\na = 10\nprint(f"A in subinterp: {a}")')
finally:
    interp.close()
