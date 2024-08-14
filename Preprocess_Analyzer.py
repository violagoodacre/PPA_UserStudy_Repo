#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[125]:


import anywidget
import traitlets
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')


# In[126]:





def to_json(instance: dict, widget) -> list[dict]:
    return {
        "df": instance["df"].to_json(orient="records")
    }


class Widget(anywidget.AnyWidget):
    _esm = """
    import * as d3 from "https://esm.sh/d3@7";

    export function render({ model, el }) {

    
    
      let df = JSON.parse(model.get("_data").df); 
      console.log(df);
      
      let df2 = JSON.parse(model.get("_data2").df); 
      console.log(df2);
      
      let df3 = JSON.parse(model.get("_data3").df); 
      console.log(df3);      

      let df_add = JSON.parse(model.get("_data4").df); 
      console.log(df_add);
      
      let df_drop = JSON.parse(model.get("_data5").df); 
      console.log(df_drop[0].mean);
      
      let df_zero = JSON.parse(model.get("_data6").df); 
      console.log("DF ZERO!");
      
      var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      svg.setAttribute('style', 'border: 1px solid black');
      svg.setAttribute('width', '1000');
      svg.setAttribute('height', '300');
      svg.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:xlink", "http://www.w3.org/1999/xlink");
      

      
      //var svg2 = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      //svg2.setAttribute('style', 'border: 1px solid black');
      //svg2.setAttribute('width', '1000');
      //svg2.setAttribute('height', '200');
      //svg2.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:xlink", "http://www.w3.org/1999/xlink");
    
      el.appendChild(svg) 
      //el.appendChild(svg2)
      
      
      d3.select(svg).append("text")
          .attr("x", 5)
          .attr("y", 15)
          .text("Removed Features");
      d3.select(svg).append("text")
          .attr("x", 5)
          .attr("y", 165)
          .text("Added Features");
      d3.select(svg)        
          .append('path')
          .attr('d', d3.line()([[0, 150], [200, 150]]))
          .attr('stroke', 'black')
      d3.select(svg)        
          .append('path')
          .attr('d', d3.line()([[200, 0], [200, 300]]))
          .attr('stroke', 'black')
          
     for (let i = 0; i < df_add.length; i++) {
          d3.select(svg).append("rect")
            .attr("x", 5)
            .attr("y", 20 + i*20)
            .attr("width", 150)
            .attr("height", 20)
            .attr("fill", "rgb(144 238 200)")
              .on("click", function(d) { 
                draw_table(df_add[i].label, df_add, df_zero);})  
     
    
          d3.select(svg).append("text")
              .attr("x", 5 )
              .attr("y", 35 + i*20)
              .text(df_add[i].label)
              .on("click", function(d) { 
                draw_table(df_add[i].label, df_add, df_zero);})
        }
          
     for (let i = 0; i < df_drop.length; i++) {
          d3.select(svg).append("rect")
            .attr("x", 5)
            .attr("y", 170 + i*20)
            .attr("width", 150)
            .attr("height", 20)
            .attr("fill", "rgb(144 238 200)")
            .on("click", function(d) {
                draw_table(df_drop[i].label, df_zero, df_drop);})
                
          d3.select(svg).append("text")
              .attr("x", 5 )
              .attr("y", 185 + i*20)
              .text(df_drop[i].label)
              .on("click", function(d) {
                draw_table(df_drop[i].label, df_zero, df_drop);})

        }          
      function draw_table(column_label, df2, df3){
          var row_index = 0
          for (let i = 0; i < df2.length; i++) {
              var curr = df2[i].label
              if (curr == column_label){
                  row_index = i
                  break;
                  }
            }

          var svg2 = document.createElementNS("http://www.w3.org/2000/svg", "svg");
          svg2.setAttribute('style', 'border: 1px solid black');
          svg2.setAttribute('width', '1000');
          svg2.setAttribute('height', '130');
          svg2.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:xlink", "http://www.w3.org/1999/xlink");
          
          el.appendChild(svg2)
          
          d3.select(svg2).append("rect")
            .attr("x", 900)
            .attr("y", 2)
            .attr("width", 80)
            .attr("height", 20)
            .attr("fill", "#FF474C")
            .on('click', function() {
                //d3.selectAll("svg2").remove();
                svg2.remove()
            });
          d3.select(svg2).append("text")
            .attr("x", 905)
            .attr("y", 18)
            .text("Remove")
            .on('click', function() {
                //d3.selectAll("svg2").remove();
                svg2.remove()
            });
          //Draw label text
           d3.select(svg2).append("text")
          .attr("x", 5)
          .attr("y", 25)
          .text(df2[row_index].label)
          
           //Draw internal tabel structure
           //Draw Horizontal lines
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[100, 10], [880, 10]]))
          .attr('stroke', 'black')
          
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[100, 40], [880, 40]]))
          .attr('stroke', 'black')
          
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[100, 70], [880, 70]]))
          .attr('stroke', 'black')

           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[100, 100], [880, 100]]))
          .attr('stroke', 'black')
          
          
          //Draw Vertical lines   
          d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[100, 10], [100, 100]]))
          .attr('stroke', 'black')  
          d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[150, 10], [150, 100]]))
          .attr('stroke', 'black')
          d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[210, 10], [210, 100]]))
          .attr('stroke', 'black')       
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[280, 10], [280, 100]]))
          .attr('stroke', 'black')        
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[340, 10], [340, 100]]))
          .attr('stroke', 'black')          
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[410, 10], [410, 100]]))
          .attr('stroke', 'black')
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[480, 10], [480, 100]]))
          .attr('stroke', 'black')      
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[540, 10], [540, 100]]))
          .attr('stroke', 'black')          
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[600, 10], [600, 100]]))
          .attr('stroke', 'black')   
          //Max 
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[660, 10], [660, 100]]))
          .attr('stroke', 'black')
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[740, 10], [740, 100]]))
          .attr('stroke', 'black')
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[820, 10], [820, 100]]))
          .attr('stroke', 'black')
           d3.select(svg2)        
          .append('path')
          .attr('d', d3.line()([[880, 10], [880, 100]]))
          .attr('stroke', 'black')
          
          //Draw Col labels
           d3.select(svg2).append("text")
          .attr("x", 110)
          .attr("y", 30)
          .text("DF")
          
           d3.select(svg2).append("text")
          .attr("x", 160)
          .attr("y", 30)
          .text("Count")
          
           d3.select(svg2).append("text")
          .attr("x", 220)
          .attr("y", 30)
          .text("Missing")
           d3.select(svg2).append("text")
          .attr("x", 290)
          .attr("y", 30)
          .text("Zeros")
           d3.select(svg2).append("text")
          .attr("x", 350)
          .attr("y", 30)
          .text("Mean")     
           d3.select(svg2).append("text")
          .attr("x", 420)
          .attr("y", 30)
          .text("Min.")   
           d3.select(svg2).append("text")
          .attr("x", 490)
          .attr("y", 30)
          .text("25%")   
           d3.select(svg2).append("text")
          .attr("x", 550)
          .attr("y", 30)
          .text("Med.")  
           d3.select(svg2).append("text")
          .attr("x", 610)
          .attr("y", 30)
          .text("75%")
           d3.select(svg2).append("text")
          .attr("x", 670)
          .attr("y", 30)
          .text("Max")          
           d3.select(svg2).append("text")
          .attr("x", 755)
          .attr("y", 30)
          .text("Std Dev.")
           d3.select(svg2).append("text")
          .attr("x", 825)
          .attr("y", 30)
          .text("Outliers")
          
          //Draw data cell
           d3.select(svg2).append("text")
          .attr("x", 110)
          .attr("y", 60)
          .text("DF1")
           d3.select(svg2).append("text")
          .attr("x", 110)
          .attr("y", 90)
          .text("DF2")
           d3.select(svg2).append("text")
          .attr("x", 165)
          .attr("y", 60)     
          .text(df2[row_index].count)
           d3.select(svg2).append("text")
          .attr("x", 165)
          .attr("y", 90)          
          .text(df3[row_index].count)
           d3.select(svg2).append("text")
          .attr("x", 225)
          .attr("y", 60)     
          .text(df2[row_index].missing)
           d3.select(svg2).append("text")
          .attr("x", 225)
          .attr("y", 90)          
          .text(df3[row_index].missing)          
           d3.select(svg2).append("text")
          .attr("x", 285)
          .attr("y", 60)     
          .text(df2[row_index].zeros)
           d3.select(svg2).append("text")
          .attr("x", 285)
          .attr("y", 90)          
          .text(df3[row_index].zeros)          
           d3.select(svg2).append("text")
          .attr("x", 345)
          .attr("y", 60)     
          .text(df2[row_index].mean)
           d3.select(svg2).append("text")
          .attr("x", 345)
          .attr("y", 90)          
          .text(df3[row_index].mean)        
           d3.select(svg2).append("text")
          .attr("x", 420)
          .attr("y", 60)     
          .text(df2[row_index].min)
           d3.select(svg2).append("text")
          .attr("x", 420)
          .attr("y", 90)          
          .text(df3[row_index].min)         
           d3.select(svg2).append("text")
          .attr("x", 485)
          .attr("y", 60)     
          .text(df2[row_index].q1)
           d3.select(svg2).append("text")
          .attr("x", 485)
          .attr("y", 90)          
          .text(df3[row_index].q1)         
           d3.select(svg2).append("text")
          .attr("x", 545)
          .attr("y", 60)     
          .text(df2[row_index].q2)
           d3.select(svg2).append("text")
          .attr("x", 545)
          .attr("y", 90)          
          .text(df3[row_index].q2)          
           d3.select(svg2).append("text")
          .attr("x", 605)
          .attr("y", 60)     
          .text(df2[row_index].q3)
           d3.select(svg2).append("text")
          .attr("x", 605)
          .attr("y", 90)          
          .text(df3[row_index].q3) 
           d3.select(svg2).append("text")
          .attr("x", 665)
          .attr("y", 60)     
          .text(df2[row_index].max)
           d3.select(svg2).append("text")
          .attr("x", 665)
          .attr("y", 90)          
          .text(df3[row_index].max)          
           d3.select(svg2).append("text")
          .attr("x", 745)
          .attr("y", 60)     
          .text(df2[row_index].std)
           d3.select(svg2).append("text")
          .attr("x", 745)
          .attr("y", 90)          
          .text(df3[row_index].std)            
           d3.select(svg2).append("text")
          .attr("x", 825)
          .attr("y", 60)     
          .text(df2[row_index].outliers)
           d3.select(svg2).append("text")
          .attr("x", 825)
          .attr("y", 90)          
          .text(df3[row_index].outliers)          
          
          return column_label
      }
      
      // Summary graphic
      
          
      var margin = {top: 40, right: 40, bottom: 40, left: 30},
        width = 750 - margin.left - margin.right,
        height = 250 - margin.top - margin.bottom;  

        var svG = d3.select(svg)
          .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .attr("x", 215)
          .append("g")
            .attr("transform",
                  "translate(" + margin.left + "," + margin.top + ")");
                      
                    
        // Create data
        var data = df

        //X scale and Axis  
        var x = d3.scaleBand()
            .range([0, width])
            .domain(data.map((d) => d.label))
            .padding(0.2)


        svG.append("g")
            .attr("id", "xaxis")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x))
            .selectAll("text")
              .attr("transform", "translate(-10,0)rotate(-20)")
              .style("text-anchor", "end"); 
              
        svG.select('#xaxis')
            .selectAll('.tick.major')
            .on("click", function(d, i) {
                console.log("LabelClick!")
                draw_table(i.label);})
              
        //Y scale and Axis
        var y = d3.scaleLinear()
          .domain([-0.5, 5])
          .range([ height, 0]);
        svG.append("g")
          .call(d3.axisLeft(y));
           
        //Bars
        svG.selectAll("mybar")
          .data(data)
          .enter()
          .append("rect")
            .attr("x", function(d) {   return x(d.label); })
            .attr("y", function(d) { return y(d.change_scale); })
            .attr("width", x.bandwidth())
            .attr("height", function(d) { return height - y(d.change_scale); })
            .attr("fill", "rgb(144 238 200)")
            .on('click', function(d, i) {
                draw_table(i.label, df2, df3)
                d3.select(this).attr("fill", "rgb(144 238 200)");
            });
        
        //Title
        svG.append("text")
          .attr("x", 250)
          .attr("y", -20)
          .text("Dataframe Change Summary");
            
        //X Label
        svG.append("text")
          .attr("x", 650)
          .attr("y", 210)
          .text("Features");            
        
        //Y Label
        svG.append("text")
          .attr("x", -30)
          .attr("y", -10)
          .text("Change Score");
               
          
        
    }

    """
    _data = traitlets.Dict().tag(sync=True, to_json=to_json)
    _data2 = traitlets.Dict().tag(sync=True, to_json=to_json)
    _data3 = traitlets.Dict().tag(sync=True, to_json=to_json)
    _data4 = traitlets.Dict().tag(sync=True, to_json=to_json)
    _data5 = traitlets.Dict().tag(sync=True, to_json=to_json)    
    _data6 = traitlets.Dict().tag(sync=True, to_json=to_json)    

    def __init__(self, df, df2, df3, df4, df5, df6):
        super().__init__(_data={"df": df}, _data2={"df": df2}, _data3={"df": df3}, _data4={"df": df4}, _data5={"df": df5}, 
                        _data6 = {"df": df6})
        #super().__init__(_data2={"df": df2})

    
    @property
    def df(self):
        return self._data["df"]

    @df.setter
    def df(self, new_df):
        self._data = { "df": new_df }
        

        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[137]:


def ppa_widget(df1_original, df2_original):
    df1 = df1_original.drop(["CountyId", "RegionId", "StateId"], axis =  1, inplace = False)
    df2 = df2_original.drop(["CountyId", "RegionId", "StateId"], axis =  1, inplace = False)
    
    common_col = np.intersect1d(df1.columns, df2.columns)
    drop_col = df1.columns.difference(df2.columns)
    add_col = df2.columns.difference(df1.columns)

    df_drop = df1[drop_col]
    df_add = df2[add_col]

    df1_com = df1[common_col]
    df2_com = df2[common_col]

    df1_num = df1_com.select_dtypes(include='number')
    df2_num = df2_com.select_dtypes(include='number')
    cat_col = np.setdiff1d(list(df1_com.columns), list(df1_num.columns))
    df1_cat = df1_com[cat_col]
    df2_cat = df2_com[cat_col]
    
    df1_num_sum = data_format(df1_num)
    df2_num_sum = data_format(df2_num)
    
    
    if df_add.empty == False:
        df_add_sum = data_format(df_add)

    else:
        data = [[0,0,0,0,0,0,0,0,"NoneAdded",0,0,0]]
        df_add_sum = pd.DataFrame(data, columns=['count', 'mean', 'std', 'min', 'q1', 'q2', 'q3', 'max', 'label', 'zeros', 'outliers', 'missing'], index = ["NoneAdded"])
    if df_drop.empty == False:
        df_drop_sum = data_format(df_drop)
    else:
        data = [[0,0,0,0,0,0,0,0,"NoneDropped",0,0,0]]
        df_drop_sum = pd.DataFrame(data, columns=['count', 'mean', 'std', 'min', 'q1', 'q2', 'q3', 'max', 'label', 'zeros', 'outliers', 'missing'], index = ["NoneDropped"])
    


    df_zero = pd.DataFrame(0, columns=df_add_sum.columns, index=df_add_sum.index)
    df_zero["label"] = df_add_sum["label"]
    df_diff = df2_num_sum[["count", "mean", "std", "min", "q1", "q2", "q3", "max", "zeros", "outliers", "missing"]].subtract(
        df1_num_sum[["count", "mean", "std", "min", "q1", "q2", "q3", "max", "zeros", "outliers", "missing"]])

    
    df_div = df_diff[["count", "mean", "std", "min", "q1", "q2", "q3", "max", "zeros", "outliers", "missing"]].div(
    df1_num_sum[["count", "mean", "std", "min", "q1", "q2", "q3", "max", "zeros", "outliers", "missing"]])
    df_div.replace([np.inf, -np.inf], 25.0, inplace=True)
    df_div.fillna(0, inplace = True)
    df_div = df_div.abs()
    df_div['change'] = df_div.sum(axis=1, numeric_only=True)
    df_div['change_log'] = df_div["change"].apply(np.log10)
    df_div["change_log"].replace([-np.inf], -2.0, inplace=True)



    scaler = MinMaxScaler(feature_range=(0, 5.0))
    df_div['change_scale'] = scaler.fit_transform(df_div['change'].values[:, None])
    df_div['change_scale'] = df_div['change_scale']

    df_div['label'] = df_div.index

    df_change = df_div[["change", "change_log", "change_scale", "label"]]
        
    return Widget(df=df_change, df2 = df1_num_sum, df3 = df2_num_sum, df4 = df_drop_sum, df5 = df_add_sum, df6 = df_zero)


# In[ ]:





# In[ ]:





# In[138]:


def my_scaler(var):
    return (5 - 0) * ( (var - min(var)) / (max(var) - min(var)) ) + 0


# In[139]:


def data_format(df1_num):
    df1_num_sum = df1_num.describe().transpose()
    df1_num_sum['label'] = df1_num_sum.index
    
    result1 = []
    for x in df1_num_sum["label"]:
        result1.append(df1_num.loc[df1_num[x].eq(0.0)].shape[0])
    df1_num_sum["zeros"] = result1
    
    result1 = []
    for index, row in df1_num_sum.iterrows():
        max = row["mean"] + 3*row["std"]
        min = row["mean"] - 3*row["std"]
        res = 0
        for x in df1_num[row["label"]]:
            if x < min or x > max:
                res = res + 1
        result1.append(res)
    df1_num_sum["outliers"] = result1
    
    result1 = []
    for x in df1_num:
        result1.append(df1_num[x].isna().sum())
    df1_num_sum["missing"] = result1
    
    df1_num_sum = df1_num_sum.rename(columns={"25%": "q1", "50%": "q2", "75%": "q3"})

    df1_num_sum["std"] = np.trunc(10 * df1_num_sum["std"]) / 10
    df1_num_sum["mean"] = np.trunc(10 * df1_num_sum["mean"]) / 10
    df1_num_sum["q1"] = np.trunc(10 * df1_num_sum["q1"]) / 10
    df1_num_sum["q2"] = np.trunc(10 * df1_num_sum["q2"]) / 10
    df1_num_sum["q3"] = np.trunc(10 * df1_num_sum["q3"]) / 10

    return df1_num_sum


# In[140]:


