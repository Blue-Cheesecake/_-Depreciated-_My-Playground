#include <stdio.h>

// 0 = available, 1 = occupied
// seat 2 2 2 2 4 4 4 4 8 8
int statusOfTable[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
// total discound for table
int totalTable[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
char equal[] = "=============================================================";
char hyphen[] = "-------------------------------------------------------------";
// temporary hold food and drink for printing out temporaring after order
int food[4] = {0, 0, 0, 0};
int drink[4] = {0, 0, 0, 0};
// Total list in each Table
// i = labeled Table
// j = quality (j in range 4 == F, j in range 4 8 == D)
int FaDTable[10][8] = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

void interfaceMainMenu()
{

    // interface
    printf("%s\nICT Restaurant System\n%s\n", equal, equal);
    printf("[1] Book a table\n[2] Order food & drink\n[3] Display and clear a bill\n[0] Exit\n");
    printf("%s\n", hyphen);
    printf("Enter the choice: ");
}

// main menu func
const char *printStatus(int status, int nums, int table)
{
    if (status == 0)
    {
        if ((table == 1 || table == 2 || table == 3 || table == 4) && nums <= 2)
        {
            return "Available";
        }
        else if ((table == 5 || table == 6 || table == 7 || table == 8) && nums <= 4)
        {
            return "Available";
        }
        else if ((table == 9 || table == 10) && nums <= 10)
        {
            return "Available";
        }
        else
        {
            return "Not enough seat";
        }
    }
    return "Occupied";
}

void bookTable()
{
    printf("[Book a table]\n");
    int numberOfPeople;
    do
    {
        printf("Enter the number of people: ");
        scanf("%d", &numberOfPeople);
        printf("\n");
        // check if nums > 0 (0 is cancel)
        int inRange = 1;
        if (numberOfPeople < 0 || numberOfPeople > 8)
        {
            inRange = 0;
            printf("Invalid number of people\n");
        }

        // print current status
        // current status refer statusofTable list
        if (numberOfPeople != 0 && inRange == 1)
        {
            // after select a table go back and ask nums of people
            // it must represent Occupied , Available, or Not enough seat
            printf("%s\nList of tables            Status\n%s\n", equal, equal);
            printf("Table 1: 2 seat          %s\n", printStatus(statusOfTable[0], numberOfPeople, 1));
            printf("Table 2: 2 seat          %s\n", printStatus(statusOfTable[1], numberOfPeople, 2));
            printf("Table 3: 2 seat          %s\n", printStatus(statusOfTable[2], numberOfPeople, 3));
            printf("Table 4: 2 seat          %s\n", printStatus(statusOfTable[3], numberOfPeople, 4));
            printf("Table 5: 4 seat          %s\n", printStatus(statusOfTable[4], numberOfPeople, 5));
            printf("Table 6: 4 seat          %s\n", printStatus(statusOfTable[5], numberOfPeople, 6));
            printf("Table 7: 4 seat          %s\n", printStatus(statusOfTable[6], numberOfPeople, 7));
            printf("Table 8: 4 seat          %s\n", printStatus(statusOfTable[7], numberOfPeople, 8));
            printf("Table 9: 8 seat          %s\n", printStatus(statusOfTable[8], numberOfPeople, 9));
            printf("Table 10: 8 seat         %s\n", printStatus(statusOfTable[9], numberOfPeople, 10));
            int numTable;
            int added = 0;
            do
            {
                printf("Enter a table number (input 0 to cancel): ");
                scanf("%d", &numTable);
                // this process can be used by loop either
                // check if status == 1 enter avaible else if num > table not enough seats
                int goAhead = 0;
                for (int i = 0; i < 10 + 1; i++)
                {
                    if (numTable == i + 1)
                    {
                        if (statusOfTable[i] == 0)
                        {
                            if (numberOfPeople <= 2 && numTable <= 4)
                            {
                                goAhead = 1;
                            }
                            else if (numberOfPeople <= 4 && numTable <= 8 && numTable > 4)
                            {
                                goAhead = 1;
                            }
                            else if (numberOfPeople <= 8 && numTable <= 10 && numTable > 8)
                            {
                                goAhead = 1;
                            }
                            if (goAhead == 1)
                            {
                                statusOfTable[i] = 1;
                                numTable = 0;
                                numberOfPeople = 0;
                            }
                            else
                            {
                                printf("Invalid choice!\n");
                            }
                        }
                        else
                        {
                            printf("Please enter the available table.\n");
                        }
                    }
                }
            } while (numTable != 0);
        }

    } while (numberOfPeople != 0);
}

void addingToClearBill(int lt, int fd, int quality)
{
    FaDTable[lt][fd] = quality;
}

void foodMenu(int labelTable)
{
    printf("\nFood Menu                       Price(Bath)\n%s\n", hyphen);
    printf("[1] Kao pad dog                 45.0\n");
    printf("[2] Squid                       45.0\n");
    printf("[3] Kung                        55.0\n");
    printf("[4] Suhi                        1.0\n%s\n", hyphen);
    int choice;
    int total = 0;
    do
    {
        printf("Enter the choice (input 0 to stop): ");
        scanf("%d", &choice);
        if (choice == 1)
        {
            total += 45;
            food[0] += 1;
        }
        else if (choice == 2)
        {
            total += 45;
            food[1] += 1;
        }

        else if (choice == 3)
        {
            total += 55;
            food[2] += 1;
        }
        else if (choice == 4)
        {
            total += 1;
            food[3] += 1;
        }
        else
        {
            if (choice != 0)
            {
                printf("Invalid choice\n");
            }
        }
    } while (choice != 0);
}

void drinkMenu(int labelTable)
{
    printf("\nDrink Menu                        Price(Bath)\n%s\n", hyphen);
    printf("[1] Coca cola                     15.0\n");
    printf("[2] Pepsi                         25.0\n");
    printf("[3] LEO                           60.0\n");
    printf("[4] Chang                         80.0\n%s\n", hyphen);
    int choice;
    int total = 0;
    do
    {
        printf("Enter the choice (input 0 to stop): ");
        scanf("%d", &choice);
        if (choice == 1)
        {
            total += 15;
            drink[0] += 1;
        }
        else if (choice == 2)
        {
            total += 25;
            drink[1] += 1;
        }

        else if (choice == 3)
        {
            total += 60;
            drink[2] += 1;
        }
        else if (choice == 4)
        {
            total += 80;
            drink[3] += 1;
        }
        else
        {
            if (choice != 0)
            {
                printf("Invalid choice\n");
            }
        }
    } while (choice != 0);
}

void orderFood()
{
    // print list of occupied table
    // check if atleast 1 occupied
    int occupied = 0;
    for (int i = 0; i < 10; i++)
    {
        if (statusOfTable[i] == 1)
        {
            occupied = 1;
        }
    }
    if (occupied == 0)
    {
        printf("You must book a table first\n");
    }
    else
    {
        printf("[Order food & drink]\n\nList of occupied tables:\n");
        for (int i = 0; i < 10; i++)
        {
            if (statusOfTable[i] == 1)
            {
                printf("Table %d\n", i + 1);
            }
        }
        printf("\n");
        int orderTable;
        do
        {
            printf("Enter the table number [1-10] (0 to exit): ");
            scanf("%d", &orderTable);
            if (orderTable >= 1 && orderTable <= 10)
            {
                // check if it orderTable has been occupied
                if (statusOfTable[orderTable - 1] == 1)
                {
                    // interface Food menu
                    printf("%s\nOrder food & drink\n%s\n", equal, equal);
                    // you need to comfirm before order
                    // if confirm True go head else return to order again
                    foodMenu(orderTable);
                    drinkMenu(orderTable);
                    printf("You have orders the following:\n");
                    for (int foodIndex = 0; foodIndex < 5; foodIndex++)
                    {
                        if (food[foodIndex] > 0)
                        {
                            switch (foodIndex)
                            {
                            case 0:
                                printf("[F] Kao pad dog  x%d\n", food[foodIndex]);
                                break;
                            case 1:
                                printf("[F] Squid  x%d\n", food[foodIndex]);
                                break;
                            case 2:
                                printf("[F] Kung  x%d\n", food[foodIndex]);
                                break;
                            case 3:
                                printf("[F] Sushi  x%d\n", food[foodIndex]);
                                break;
                            default:
                                break;
                            }
                        }
                    }
                    for (int dIndex = 0; dIndex < 5; dIndex++)
                    {
                        if (drink[dIndex] > 0)
                        {
                            switch (dIndex)
                            {
                            case 0:
                                printf("[D] Coca cola x%d\n", drink[dIndex]);
                                break;
                            case 1:
                                printf("[D] Pepsi x%d\n", drink[dIndex]);
                                break;
                            case 2:
                                printf("[D] Leo x%d\n", drink[dIndex]);
                                break;
                            case 3:
                                printf("[D] Chang x%d\n", drink[dIndex]);
                                break;
                            default:
                                break;
                            }
                        }
                    }
                    int confirm;
                    printf("Confirm? (y|n) (1 for yes, 0 for no): ");
                    scanf("%d", &confirm);
                    if (confirm == 1)
                    {
                        for (int j = 0; j < 4; j++)
                        {
                            if (food[j] > 0)
                            {
                                switch (j)
                                {
                                case 0:
                                    totalTable[orderTable - 1] += (food[j] * 45);
                                    addingToClearBill(orderTable - 1, 0, food[j]);
                                    break;
                                case 1:
                                    totalTable[orderTable - 1] += (food[j] * 45);
                                    addingToClearBill(orderTable - 1, 1, food[j]);
                                    break;
                                case 2:
                                    totalTable[orderTable - 1] += (food[j] * 55);
                                    addingToClearBill(orderTable - 1, 2, food[j]);
                                    break;
                                case 3:
                                    totalTable[orderTable - 1] += (food[j] * 1);
                                    addingToClearBill(orderTable - 1, 3, food[j]);
                                    break;
                                default:
                                    break;
                                }
                            }
                            if (drink[j] > 0)
                            {
                                switch (j)
                                {
                                case 0:
                                    totalTable[orderTable - 1] += (drink[j] * 15);
                                    addingToClearBill(orderTable - 1, 4, drink[j]);
                                    break;
                                case 1:
                                    totalTable[orderTable - 1] += (drink[j] * 25);
                                    addingToClearBill(orderTable - 1, 5, drink[j]);
                                    break;
                                case 2:
                                    totalTable[orderTable - 1] += (drink[j] * 60);
                                    addingToClearBill(orderTable - 1, 6, drink[j]);
                                    break;
                                case 3:
                                    totalTable[orderTable - 1] += (drink[j] * 80);
                                    addingToClearBill(orderTable - 1, 7, drink[j]);
                                    break;
                                default:
                                    break;
                                }
                            }
                        }
                    }
                    // however either n or y list shoud be reset
                    // reset
                    for (int j = 0; j < 5; j++)
                    {
                        food[j] = 0;
                        drink[j] = 0;
                    }
                    orderTable = 0;
                }
                else
                {
                    printf("You didn't book this table yet\n");
                }
            }
            else
            {
                printf("Invalid\n");
            }

        } while (orderTable != 0);
    }
}

// clear a bill each table
void displayAndClearABill()
{
    // checl if occupied or not
    int occupied = 0;
    for (int i = 0; i < 10; i++)
    {
        if (statusOfTable[i] == 1)
        {
            occupied = 1;
        }
    }
    if (occupied == 0)
    {
        printf("You must book a table first\n");
    }
    else
    {
        printf("[Display and clear a bill]\n\n");
        printf("List of occupied table:\n");
        for (int i = 0; i < 10; i++)
        {
            if (statusOfTable[i] == 1)
            {
                printf("Table %d\n", i + 1);
            }
        }
        int orderTable;
        do
        {
            printf("Enter the table number [1-10] (0 to exit): ");
            scanf("%d", &orderTable);
            if (orderTable >= 1 && orderTable <= 10)
            {
                if (statusOfTable[orderTable - 1] == 1)
                {
                    // check if order Table atleast order Food or drink
                    int atleastForD = 0;
                    for (int k = 0; k < 8; k++)
                    {
                        if (FaDTable[orderTable - 1][k] > 0)
                        {
                            atleastForD = 1;
                        }
                    }
                    if (atleastForD == 0)
                    {
                        printf("\nThere is no any ordered food or drink\n");
                    }
                    else
                    {
                        printf("\nYou have order the following:\n\n");
                        printf("Food menu                    Qty.   Price (Bath)\n%s\n", hyphen);
                        int atleastFood = 0;
                        for (int i = 0; i < 4; i++)
                        {
                            if (FaDTable[orderTable - 1][i] != 0)
                            {
                                atleastFood = 1;
                                int qty = FaDTable[orderTable - 1][i];
                                switch (i)
                                {
                                case 0:
                                    printf("[%d] Kao pad dog               %d     %d\n", i + 1, qty, qty * 45);
                                    break;
                                case 1:
                                    printf("[%d] Squid                     %d     %d\n", i + 1, qty, qty * 45);
                                    break;
                                case 2:
                                    printf("[%d] Kung                      %d     %d\n", i + 1, qty, qty * 55);
                                    break;
                                case 3:
                                    printf("[%d] Sushi                     %d     %d\n", i + 1, qty, qty * 1);
                                    break;
                                default:
                                    break;
                                }
                            }
                        }
                        if (atleastFood == 0)
                        {
                            printf("None\n");
                        }
                        printf("%s\n\n", hyphen);
                        printf("Drink menu                   Qty.   Price (Bath)\n%s\n", hyphen);
                        int atleastDrink = 0;
                        for (int j = 4; j < 8; j++)
                        {
                            if (FaDTable[orderTable - 1][j] != 0)
                            {
                                atleastDrink = 1;
                                int qty = FaDTable[orderTable - 1][j];
                                switch (j)
                                {
                                case 4:
                                    printf("[%d] Coca cola                 %d     %d\n", j - 3, qty, qty * 15);
                                    break;
                                case 5:
                                    printf("[%d] Pepsi                     %d     %d\n", j - 3, qty, qty * 25);
                                    break;
                                case 6:
                                    printf("[%d] Leo                       %d     %d\n", j - 3, qty, qty * 60);
                                    break;
                                case 7:
                                    printf("[%d] Chang                     %d     %d\n", j - 3, qty, qty * 80);
                                    break;
                                default:
                                    break;
                                }
                            }
                        }
                        if (atleastDrink == 0)
                        {
                            printf("None\n");
                        }
                        printf("%s\n\n", hyphen);
                        printf("** Total amount: %d\n\n", totalTable[orderTable - 1]);
                        int confirm;
                        printf("Do you want to clear a bill? (y|n) (1 for yes, 0 for no): ");
                        scanf("%d", &confirm);
                        printf("\n");
                        if (confirm == 1)
                        {
                            // reset occupied, total, and order in FaDTable
                            totalTable[orderTable - 1] = 0;
                            for (int fd = 0; fd < 8; fd++)
                            {
                                FaDTable[orderTable][fd] = 0;
                            }
                            statusOfTable[orderTable - 1] = 0;
                            orderTable = 0;
                        }
                        else
                        {
                            orderTable = 0;
                        }
                    }
                }
                else
                {
                    printf("You must occupied this table first\n");
                }
            }
            else
            {
                printf("Invalid table\n");
            }

        } while (orderTable != 0);
    }
}

int main()
{
    int choice;
    int True = 1;
    while (True == 1)
    {
        interfaceMainMenu();
        scanf("%d", &choice);
        if (choice == 0)
        {
            True = 0;
            break;
        }
        else
        {
            if (choice == 1)
            {
                bookTable();
            }
            else if (choice == 2)
            {
                orderFood();
            }
            else if (choice == 3)
            {
                displayAndClearABill();
            }
            else
            {
                printf("Invalid command");
            }
        }
    }
    return 0;
}