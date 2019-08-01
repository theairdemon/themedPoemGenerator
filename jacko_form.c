#include <stdio.h>

int main (const int argc, const char *argv[])
{
    printf("Please fill out the following form \n");
    printf("Job title, such as 'analyst':");
    char jobTitle[200];
    scanf("%s", &jobTitle[0]); printf("\n");
    printf("Company: ");
    char company[200];
    scanf("%s", &company[0]); printf("\n"); 
    printf("First thing you find on their website: ");
    char firstThing[200];
    scanf("%s", &firstThing[0]); printf("\n");
    printf("Brief description of something that qualifies you to work there:");
    char qualification[400];
    scanf("%s", &qualification[0]); printf("\n");
    printf("Passion 1: ");
    char firstPassion[200];
    scanf("%s", &firstPassion[0]); printf("\n");
    printf("Passion 2: ");
    char secondPassion[200];
    scanf("%s", &secondPassion[0]); printf("\n");

    printf("Lesser company: ");
    char lesserCompany[200];
    scanf("%s", &lesserCompany[0]); printf("\n");
    printf("Vague positive adjective: ");
    char vagueAdj[200];
    scanf("%s", &vagueAdj[0]); printf("\n");
    printf("Action word / menial task 1:");
    char actionWord1[200];
    scanf("%s", &actionWord1[0]); printf("\n");
    printf("Action word / menial task 2: ");
    char actionWord2[200];
    scanf("%s", &actionWord2[0]); printf("\n");
    printf("Antonym for crying in the bathroom: "); 
    char antonymCrying[200];
    scanf("%s", &antonymCrying[0]); printf("\n");
    printf("Verb for completely fucking something up and scrambling to cover it while getting yelled at by my boss:");
    char verbFuck[200];
    scanf("%s", &verbFuck[0]); printf("\n");

    printf("Adjective: ");
    char adj1[200];
    scanf("%s", &adj1[0]); printf("\n");
    printf("Adverb:");
    char adv1[200];
    scanf("%s", &adv1[0]); printf("\n");
    printf("Any math word you know (just put down 'median' you dumb fuck): ");
    char mathWord[200];
    scanf("%s", &mathWord[0]); printf("\n");
    printf("Synonym for 'slack off and still manage to get a gentlemen's B+': ");
    char slacker[200];
    scanf("%s", &slacker[0]); printf("\n");

    printf("Your one redeeming quality: ");
    char redeemable[200];
    scanf("%s", &redeemable[0]); printf("\n");
    printf("Pick a random word, they're not even reading this anymore: ");
    char randomWord[200];
    scanf("%s", &randomWord[0]); printf("\n");
    printf("Say what the company does: ");
    char evilShit[200];
    scanf("%s", &evilShit[0]); printf("\n");
    printf("Element of toxic workplace culture: ");
    char toxic[200];
    scanf("%s", &toxic[0]); printf("\n");
    for (int i = 0; i < 50; i++){
        printf("\n");
    }
    printf("To whom it may concern: \n \n");
    printf("I am interested in the %s position at %s. I believe that I am a good fit for your company because of your focus on %s. My qualifications are %s. My academic experience reflects my passion for %s and %s.\n \n", jobTitle, company, firstThing, qualification, firstPassion, secondPassion);
    printf("In my time at %s, I gained a %s skill set I could apply during my %s internship. As an intern, my responsibilities included %s, %s, and %s. I gained problem-solving experience by %s. \n \n", lesserCompany, vagueAdj, actionWord1, actionWord2, antonymCrying, verbFuck);
    printf("I developed quantitative skills through my economics coursework. Given a %s set of data, I was able to %s calculate the %s. I used complex modeling to find how much I could %s. \n \n", adj1, adv1, mathWord, slacker);
    printf("I also am committed to extracurricular activities, such as pong. I was selected by my peers to represent them in Masters C, where I pulled trig a total of 5 times. I was elected without contest as a member of student government, where m responsibilities included ?????. \n \n");
    printf("If you company could use a %s who is passionate about %s, I would be honored to engage in %s. Your company's %s sounds like the perfect fit for me.\n \n", redeemable, randomWord, evilShit, toxic);
    printf("Sincerely, \n Imma Badperson \n");





}