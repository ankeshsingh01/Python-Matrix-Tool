import numpy as np

def get_matrix(name):
    print(f"\nEnter elements for {name}:")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print(f"Enter the {rows*cols} elements space-separated:")
    elements = list(map(float, input().split()))
    return np.array(elements).reshape(rows, cols)

def main():
    print("--- Matrix Operations Tool ---")
    
    while True:
        print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose\n5. Determinant\n6. Exit")
        choice = input("Select an operation (1-6): ")

        if choice == '6':
            break

        try:
            # Transpose and Determinant only need one matrix
            if choice in ['4', '5']:
                mat = get_matrix("Matrix")
                if choice == '4':
                    print("Result:\n", mat.T)
                else:
                    print("Determinant:", np.linalg.det(mat))
            
            # Others need two matrices
            elif choice in ['1', '2', '3']:
                a = get_matrix("Matrix A")
                b = get_matrix("Matrix B")
                
                if choice == '1':
                    print("Result:\n", np.add(a, b))
                elif choice == '2':
                    print("Result:\n", np.subtract(a, b))
                elif choice == '3':
                    print("Result:\n", np.dot(a, b))
            else:
                print("Invalid choice!")
        except Exception as e:
            print(f"Error: {e}. (Ensure dimensions match for the operation!)")

if __name__ == "__main__":
    main()