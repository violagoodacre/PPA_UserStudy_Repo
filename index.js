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
        } // end for
          
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

        } // end for         
        
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