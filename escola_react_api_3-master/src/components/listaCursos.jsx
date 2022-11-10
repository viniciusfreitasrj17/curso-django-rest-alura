import React, { Component } from 'react';

class ListaCursos extends Component {
    state = {
        data: [],
        loaded: false,
        error: null,
    }

    componentDidMount() {
        fetch("http://127.0.0.1:9000/courses/")
          .then(response => {
            console.log(response);
            if (response.status > 400) {
            // Código do comportamento em caso de problema na req
            }
            return response.json();
          })
          .then(data => {
            this.setState(() => {
              return {
                data,
                loaded: true
              };
            });
          })
          .catch(e => {
            this.setState(() => {
              return {
                error: e.message,
                loaded: false,
                data: []
              };
            });
          });
      }
    
      render() {
        return (
            <div>
            {
              this.state.error
            ? 
              (
                <h1>{this.state.error.toString()}</h1>
              )
            : 
              this.state.data.map(curso => {
                return (
                  <h2 key={curso.id} className='App-table'>
                    {curso.description}
                  </h2>
                );
              })}
          </div>
        );
      }
    }

export default ListaCursos;