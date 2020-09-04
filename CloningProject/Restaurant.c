#include <stdio.h>

// index -->
// Menu function = line 12
// The BookTable function is done
// Book table function = line 48
// Order food & drink function = line

// 0 = available, 1 = occupied
// seat 2 2 2 2 4 4 4 4 8 8
int statusOfTable[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
// total discound for table
int totalTable[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
char equal[] = "===================";
char hyphen[] = "--------------------";
int food[4] = {0, 0, 0, 0};
int drink[4] = {0, 0, 0, 0};

void interfaceMainMenu()
{

    // interface
    printf("%s\nICT Restaurant System\n%s\n", equal, equal);
    printf("[1] Book a table\n[2] Order food & drink\n[3] Display and clear a bill\n[0] Exit\n");
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
            // *Bug --> if put 8 the seat 2 and 4 must represent Not enogh eeat
            printf("%s\nList of tables               Status\n%s\n", equal, equal);
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

void foodMenu(int labelTable)
{
    printf("%s\nFood Menu                   Price(Bath)\n", hyphen);
    printf("[1] Kao pad dog                 45.0\n");
    printf("[2] Squid                       45.0\n");
    printf("[3] Kung                        55.0\n");
    printf("[4] O rama                      1.0\n%s\n", hyphen);
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
            printf("Invalid choice\n");
        }

    } while (choice != 0);
}

void drinkMenu(int labelTable)
{
    printf("%s\nDrink Menu                    Price(Bath)\n", hyphen);
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
            printf("Invalid choice\n");
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
                    char confirm;
                    printf("Confirm? (y|n): ");
                    scanf("%c", &confirm);
                    if (confirm == 'y')
                    {
                        for (int j = 0; j < 5; j++)
                        {
                            if (food[j] > 0)
                            {
                                switch (j)
                                {
                                case 0:
                                    totalTable[orderTable - 1] += (j * 45);
                                    break;
                                case 1:
                                    break;
                                case 2:
                                    break;
                                case 3:
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
                                    break;
                                case 1:
                                    break;
                                case 2:
                                    break;
                                case 3:
                                    break;
                                default:
                                    break;
                                }
                            }
                        }
                    }
                    else if (confirm == 'n')
                    {
                        // reset
                        for (int j = 0; j < 5; j++)
                        {
                            food[j] = 0;
                            drink[j] = 0;
                        }
                    }
                }
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
                printf("Clear");
            }
            else
            {
                printf("Invalid command");
            }
        }
    }
    for (int i = 0; i < 10; i++)
    {
        printf("%d %d\n", statusOfTable[i], totalTable[i]);
    }

    return 0;
}