import sys
from get_last import last, euro_last, primi_last, bono_last
from upd_sheet import euro_sheet, primi_sheet, bono_sheet

# update euro 2
num_comb = 1
if len (sys.argv) < 2:
    print("update [euro|primi|bono] #combinaciones")
    num_comb = sys.argv[2]
    exit()

if sys.argv[1] == "euro":
    combs = euro_last(last('EMIL',num_comb))
    euro_sheet(combs)

if sys.argv[1] == "primi":
    combs = primi_last(last('LAPR',num_comb))
    primi_sheet(combs)

if sys.argv[1] == "bono":
    combs = bono_last(last('BONO',num_comb))
    bono_sheet(combs)