
from Person import Person
from flask import Flask,  render_template, Blueprint, request
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

#Take in the input number
class input_form(FlaskForm):
    
    number = IntegerField('number', 
                            validators=[DataRequired(), 
                            ])


class IndividualMaker:
    def __init__(self, n):
        self.males = []
        self.females = []

        for i in range(0,n):
            self.males.append(Person(i, "male", n ))
            self.females.append(Person(i, "female", n))


    def paired(self):
        for man in self.males:
            if not man.partner:
                return False
        return True


    def pair(self, man, woman):
        man.partner = woman
        woman.partner = man
        #created an output dict to pass into template
        output_dict[man] = woman

    def free(self, man, woman):
        man.partner = None
        woman.partner = None


    def StableMatch(self):
        #till everyone has a partner
        while not self.paired():
            for man in self.males:
                if not man.partner:
                    for i in man.available_proposals:
                        #match with the first woman
                        if not self.females[i].partner:
                            self.pair(man, self.females[i])
                            man.available_proposals.remove(i)
                            break
                        #check the preference with the current partner
                        elif self.females[i].partner and self.females[i].get_preference(man.id) < self.females[i].get_preference(self.females[i].partner.id):
                            self.free(self.females[i].partner, self.females[i])
                            self.pair(man, self.females[i])
                            break



app = Flask(__name__)

@app.route('/',  methods=['GET','POST'])
def start_match():  # put application's code here
    #removing cache
    output_dict.clear()

    #get the input from the form
    if request.method == 'POST':
        number = request.form.get('number')

        dataSet = IndividualMaker(int(number))
        #call function 
        dataSet.StableMatch()
    return render_template("graph.html", data = output_dict )

output_dict = {}
if __name__ == '__main__':
    app.run()


    
