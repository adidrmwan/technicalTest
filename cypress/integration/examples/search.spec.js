/// <reference types="cypress" />

describe('Search Function', function() {
    context('Search', () => {
        before(() => {
          cy.fixture('testDataProduct').then(function(product) {
            this.data = product
          }) 
        })

        it('search product', function() {
          let len = Object.keys(this.data).length;
          cy.visit('qa.fabelio.com')
            if( len > 1 ) {
                for( let x = 0; x < len; x++) {
                  cy.get('input[placeholder="Cari produk"]').click()
                  cy.get('input[placeholder="Cari produk"]').type(this.data[x].name)
                  cy.wait(3000)
                  cy.get('section > div > a').click()
                  cy.wait(3000)
                  cy.get('#'+this.data[x].id).scrollIntoView({ easing: 'linear' }).should('be.visible').then((product) => {
                      if(product) {
                          cy.get('#'+this.data[x].id +'> .css-1eanzts > .no-highlight > .start > .css-w11x8x').click()
                      }
                  })
                  cy.wait(5000)
                  cy.get('#addToCart').should('be.visible').then((addToCart) => {
                      Cypress.$(addToCart).click()
                  })
                  cy.wait(5000)
                  if(x < len-1) {
                    cy.get('input[placeholder="Cari produk"]').clear()
                  }
                }
                cy.get('a[aria-label="Keranjang Saya"]').click()
                cy.get('div[role="presentation"] > .MuiList-root > .MuiListItem-root > .MuiGrid-container > .MuiGrid-item > .MuiBox-root > .MuiBox-root').should('have.text','Troli Belanja'+len+' Barang')
            }
            else  {
              cy.get('input[placeholder="Cari produk"]').click()
                cy.get('input[placeholder="Cari produk"]').type(this.data[0].name)
                cy.wait(3000)
                cy.get('section > div > a').click()
                cy.wait(3000)
                cy.get('#'+this.data[0].id).scrollIntoView({ easing: 'linear' }).should('be.visible').then((product) => {
                    if(product) {
                        cy.get('#'+this.data[0].id +'> .css-1eanzts > .no-highlight > .start > .css-w11x8x').click()
                    }
                })
                cy.wait(5000)
                cy.get('#addToCart').should('be.visible').then((addToCart) => {
                    Cypress.$(addToCart).click()
                })
                cy.wait(5000)
                cy.get('a[aria-label="Keranjang Saya"]').click()
                cy.get('div[role="presentation"] > .MuiList-root > .MuiListItem-root > .MuiGrid-container > .MuiGrid-item > .MuiBox-root > .MuiBox-root').should('have.text','Troli Belanja1 Barang')
                cy.wait(2000)
              }
            const today = Cypress.moment()
            cy.screenshot('result'+today);
        })
    })
})