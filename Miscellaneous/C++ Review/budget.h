#ifndef BUDGET_H
#define BUDGET_H

class Budget{
    private:
        static double corpBudget;
        double divisionBudget;
    public:
        Budget(){
            divisionBudget=0;
        }
        void addBudget(double b){
            divisionBudget+=b;
            corpBudget+=b;
        }
        double getDivisonBudget() const{
            return divisionBudget;
        }
        double getCorpBudget() const{
            return corpBudget;
        }
};
#endif