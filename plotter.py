import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filename = 'rawdata.csv'
df = pd.read_csv(filename)
print(df)
print(df.columns[0])
print("mean",df.mean())


gene_row_list = list(df['Gene'])
gene_col_list = list(df.columns)
gene_col_list.pop(0)

# test_gene = ['ND1','ND4','ND5','ND6','CYTB']
test_gene = ['CYTB']
for gene in test_gene:

    gene_idx = gene_row_list.index(gene)

    gene_list = []


    data = df.iloc[gene_idx]
    for j in range(1,len(df.columns)):
        gene_list.append(data[df.columns[j]])

    print("-----------------------------------------------")

    sorted_gene = [x for _,x in sorted(zip(gene_list,gene_col_list), reverse=False)]
    sorted_val = [x for x,_ in sorted(zip(gene_list,gene_col_list), reverse=False)]
    sorted_gene.reverse()
    sorted_val.reverse()
    
    print(gene)
    print(sorted_gene)
    


    result_df = pd.DataFrame({'gene_col': sorted_gene,
                            'gene_val': sorted_val})
    print(result_df)

    
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('test2png.png', dpi=100)

    sns.barplot(data=result_df, x='gene_col', y='gene_val')
    plt.title(gene)
    plt.xticks(rotation=90)
    plt.grid(which='both')
    fig.savefig(gene+'.png', dpi=100)
    # plt.show()

