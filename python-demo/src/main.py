
import utils as ut;

if __name__ == "__main__":
    name="Alice";
    print(ut.greet(name));
    print(ut.farewellMsg(name));
    a, b = 10, 5;
    print(f"Addition: {ut.add(a, b)}");
    print(f"Subtraction: {ut.subtract(a, b)}");
    print(f"Multiplication: {ut.multiply(a, b)}");
    print(f"Division: {ut.divide(a, b)}");