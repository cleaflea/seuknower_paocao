class CreateTyxMessages < ActiveRecord::Migration
  def change
    create_table :tyx_messages do |t|
      t.text :message

      t.timestamps
    end
  end
end
