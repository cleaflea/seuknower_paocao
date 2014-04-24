class PaocaoController < ApplicationController
    def index
        @paocaomessage = ""
        File.open("./paocaomessage", "r") do |file|
            while line = file.gets
                @paocaomessage += line
            end
        end
    end

    def service
        @paocaomessage = ""
        File.open("./paocaomessage", "r") do |file|
            while line = file.gets
                @paocaomessage += line
            end
        end
        render :json => {:message => @paocaomessage}
    end
end
