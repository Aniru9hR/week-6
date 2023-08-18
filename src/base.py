import pandas as pd


class Base:
    def __init__(self): 
        self.mat_df = pd.read_csv(r"C:\Users\aniru\OneDrive\Documents\codingtemple\week6\day3\student\student-mat.csv", sep=';')
        self.por_df = pd.read_csv(r"C:\Users\aniru\OneDrive\Documents\codingtemple\week6\day3\student\student-por.csv", sep=';')
        self.get_data()
    
    def get_data(self):
        self.df = pd.concat([self.mat_df, self.por_df])
        self.df.columns = self.df.columns.str.lower()
        self.df.columns = ['school','sex','age','address','fam_size','p_status','m_edu','f_edu',
           'm_job','f_job','reason','guardian','travel_time','study_time','failures','school_sup',
          'fams_up','paid','activities','nursery','higher','internet','romantic','fam_rel',
          'free_time','go_out','dalc','walc','health','absences','g1','g2','g3']   
        print(self.df)
        return self.df


if __name__ == '__main__':
    c = Base()
    c.get_data()