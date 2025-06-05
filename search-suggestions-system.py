class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggests=[]
        for ind in range(0,len(searchWord)):
            currSearch = searchWord[:ind+1]
            tempSuggests = []
            for product in products:
                if(product.startswith(currSearch) and len(tempSuggests)<3):
                    tempSuggests.append(product)
            suggests.append(tempSuggests)
        return suggests
            
        
