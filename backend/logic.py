import spacy
from typing import Tuple


class Analyzer:
    def __init__(self, text: str):
        self.text = text
    
    @staticmethod
    def get_organizations(text: str) -> list:
        nlp = spacy.load("en_core_web_sm")

        doc = nlp(text)
        orgs = []
        for ent in doc.ents:
            if ent.label_ in ('ORG'):
                orgs.append(ent.text)
                
        return orgs
    
    @staticmethod
    def standartisation(orgs: list) -> Tuple[set, list]:
        orgs_filter = ['co.', 'company', 'corp.', 'corp', 'corparation', 'co.’s']
        for i in range(len(orgs)):
            for corp_filter in orgs_filter:
                orgs_splited = orgs[i].lower().split()
                try:
                    index = orgs_splited.index(corp_filter)
                    orgs_splited[index] = 'company'
                    orgs[i] = ' '.join(orgs_splited).title()
                except ValueError:
                    pass

        orgs_set = set(orgs)
        standartisite_orgs_set = orgs_set.copy()
        for org in orgs_set:
            for next_org in orgs_set:
                if org in next_org and len(next_org) > len(org):
                    standartisite_orgs_set.remove(next_org)
                    orgs.append(org)
                    
        standartisite_orgs_list = []
        for org in orgs:
            if org in standartisite_orgs_set:
                standartisite_orgs_list.append(org)
        return standartisite_orgs_set, standartisite_orgs_list

    def get_most_recent_organization(self, orgs: list) -> str:
        orgs_set, orgs_list = self.standartisation(orgs)
        org_dict = {}
        for org in orgs_set:
            org_dict[org] = orgs_list.count(org)
            
        return max(org_dict, key=org_dict.get)
        
    def parse(self) -> str:
        orgs = self.get_organizations(self.text)
        if orgs:
            return self.get_most_recent_organization(orgs)
        else:
            return ''
