from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit == "C":
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        return value, f, k
    elif unit == "F":
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        return c, value, k
    elif unit == "K":
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        return c, f, value
    else:
        return None

def main():
    console.print("[bold cyan]🌡️  Welcome to the Advanced Temperature Converter![/bold cyan]")

    while True:
        try:
            value = float(Prompt.ask("Enter the temperature value"))
            unit = Prompt.ask("Enter the unit of measurement", choices=["C", "F", "K"], default="C")

            results = convert_temperature(value, unit)
            if results:
                c, f, k = results
                table = Table(title="Converted Temperature Values")
                table.add_column("Scale", style="bold magenta")
                table.add_column("Value", style="bold green")

                table.add_row("Celsius (°C)", f"{c:.2f}")
                table.add_row("Fahrenheit (°F)", f"{f:.2f}")
                table.add_row("Kelvin (K)", f"{k:.2f}")

                console.print(table)
            else:
                console.print("[red]Invalid unit entered![/red]")

        except ValueError:
            console.print("[red]⚠️ Please enter a valid numeric temperature![/red]")
            continue

        again = Prompt.ask("Do you want to convert another temperature?", choices=["yes", "no"], default="yes")
        if again.lower() == "no":
            console.print("[bold green]✅ Thank you for using the Temperature Converter! Goodbye![/bold green]")
            break

if __name__ == "__main__":
    main()
