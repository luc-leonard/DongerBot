import shlex


#TODO : ID avec des GUID (courts), non sequenciels
class Poller():
    def __init__(self):
        self.current_poll_id = 0
        self.polls = {}

    def makePoll(self, auteur, options):
        splitted_options = shlex.split(options)
        question = splitted_options[0]
        answers = splitted_options[1:]
        newPoll = Poll(auteur, question, answers)
        self.polls[str(self.current_poll_id)] = newPoll
        pol_id = self.current_poll_id
        self.current_poll_id = self.current_poll_id + 1
        return "NEW POLL: " + question + "\r\nTO VOTE USE !vote " + str(pol_id) + " <choice>\r\n TO GET RESULTS USE !sondage_resultat " + str(pol_id)

    def voteFor(self, auteur, poll_id, option):
        if poll_id not in self.polls:
            return "no such poll"
        opt = shlex.split(option)
        print opt
        return self.polls[poll_id].voteFor(auteur, opt[1])

    def getResult(self, poll_id):
        if poll_id not in self.polls:
            return "no such poll"
        return self.polls[poll_id].question + " => " + self.polls[poll_id].getResult()


class Poll():
    def __init__(self, auteur, question, answers):
        self.question = question
        self.answers = {i: 0 for i in answers}
        self.hasVoted = []

    def voteFor(self, auteur, option):
        if auteur in self.hasVoted:
            return auteur + " has already voted"
        if option not in self.answers.keys():
            return option + " is not an answer to " + self.question
        self.answers[option] = self.answers[option] + 1
        self.hasVoted.append(auteur)
        return auteur + " has voted"

    def getResult(self):
        return str(self.answers) + "\r\n voteurs: " + str(self.hasVoted)
