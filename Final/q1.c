/*  -----  Please fill in your information in this comment block -----  
   Student ID: 6388073
   Fullname: Sinut Wattnarporn
   Section: 3
---------------------------------------------------------------------- */

/*  ===== Put your code here ===== */

#include <stdio.h>

struct Item
{
    char item_name[21];
    int quantity;
    float price;
    int is_taxed;
};

struct Order
{
    int order_id;
    char customer_name[21];
    struct Item items[3];
    float total;
    float vat_refund;
};

int main()
{
    int n;
    scanf("%d", &n);
    struct Order orders[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &orders[i].order_id);
        scanf("%s", orders[i].customer_name);
        for (int j = 0; j < 3; j++)
        {
            scanf("%s", orders[i].items[j].item_name);
            scanf("%d", &orders[i].items[j].quantity);
            scanf("%f", &orders[i].items[j].price);
            scanf("%d", &orders[i].items[j].is_taxed);
        }
    }

    for (int i = 0; i < n; i++)
    {
        float sum = 0;
        float vat_re = 0;
        printf("Order#%d from %s\n", orders[i].order_id, orders[i].customer_name);
        for (int j = 0; j < 3; j++)
        {
            sum += (orders[i].items[j].price * orders[i].items[j].quantity);
            if (orders[i].items[j].is_taxed == 1)
            {
                float vat = 0.07;
                float plus = orders[i].items[j].price * orders[i].items[j].quantity * vat;
                vat_re += plus;
            }
        }
        printf("Total: %.2f VAT-refunded: %.2f\n", sum, vat_re);
    }

    // ? debug purpose
    // for (int i = 0; i < n; i++)
    // {
    //     printf("%d %s\n", orders[i].order_id, orders[i].customer_name);
    //     for (int j = 0; j < 3; j++)
    //     {
    //         printf("%s ", orders[i].items[j].item_name);
    //         printf("%d ", orders[i].items[j].quantity);
    //         printf("%f ", orders[i].items[j].price);
    //         printf("%d", orders[i].items[j].is_taxed);
    //         printf("\n");
    //     }
    //     printf("\n");
    // }
}